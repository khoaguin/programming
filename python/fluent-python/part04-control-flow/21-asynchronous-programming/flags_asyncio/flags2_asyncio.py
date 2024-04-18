#!/usr/bin/env python3

"""Download flags of countries (with error handling).

asyncio async/await version

"""
# tag::FLAGS2_ASYNCIO_TOP[]
import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path

import httpx
import tqdm  # type: ignore

from flags2_common import main, DownloadStatus, save_flag

# low concurrency default to avoid errors from remote site,
# such as 503 - Service Temporarily Unavailable
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

async def get_flag(
    client: httpx.AsyncClient,
    base_url: str,
    cc: str
) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = await client.get(  # `.get` is an `AsyncClient` method, 
                            # and it’s a coroutine, so we need to `await` it
        url, timeout=3.1, follow_redirects=True
    )
    resp.raise_for_status()
    return resp.content

async def download_one(
    client: httpx.AsyncClient,
    cc: str,
    base_url: str,
    semaphore: asyncio.Semaphore,
    verbose: bool,
) -> DownloadStatus:
    try:
        async with semaphore:  # Use the semaphore as an asynchronous context manager so that the program as a
                            # whole is not blocked; only this coroutine is suspended when the semaphore
                            # counter is zero
            image = await get_flag(client, base_url, cc)
    except httpx.HTTPStatusError as exc:
        res = exc.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'not found: {res.url}'
        else:
            raise
    else:
        await asyncio.to_thread(  # Saving the image is an I/O operation. To avoid 
                                # blocking the event loop, run
                                # `save_flag` in a thread.
            save_flag, image, f'{cc}.gif'
        )
        status = DownloadStatus.OK
        msg = 'OK'
    if verbose and msg:
        print(cc, msg)
    return status
# end::FLAGS2_ASYNCIO_TOP[]

# tag::FLAGS2_ASYNCIO_START[]
async def supervisor(
    cc_list: list[str],
    base_url: str,
    verbose: bool,
    concur_req: int
) -> Counter[DownloadStatus]:
    """
    supervisor has the same args with `download_many` below, but it can't be run 
    directly in main since it's a coroutine
    """
    counter: Counter[DownloadStatus] = Counter()
    semaphore = asyncio.Semaphore(concur_req)  # Create an `asyncio.Semaphore` that 
                                            # will not allow more than `concur_req` active
                                            # coroutines among those using this semaphore
    async with httpx.AsyncClient() as client:
        to_do = [download_one(client, cc, base_url, semaphore, verbose)
                for cc in sorted(cc_list)]  # Create a list of coroutine objects, 
                                        # one per call to the `download_one` coroutine
        to_do_iter = asyncio.as_completed(to_do)  # Get an iterator that will return
                                                # coroutine objects as they are done
        if not verbose:
            to_do_iter = tqdm.tqdm(
                to_do_iter, total=len(cc_list)
            )  # Wrap the `as_completed` iterator with the tqdm generator function to display progress.
        error: httpx.HTTPError | None = None  # used to hold an exception beyond the try/except statement, if one is raised
        for coro in to_do_iter:
            try:
                status = await coro  # await on the coroutine to get its result. 
                                    # This will not block because as_completed only produces coroutines that are done
            except httpx.HTTPStatusError as exc:
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=exc.response)
                error = exc
            except httpx.RequestError as exc:
                error_msg = f'{exc} {type(exc)}'.strip()
                error = exc
            except KeyboardInterrupt:
                break

            if error:
                status = DownloadStatus.ERROR  # If there was an error, set the status.
                if verbose:
                    url = str(error.request.url)  # In verbose mode, extract the URL from the exception that was raised…
                    cc = Path(url).stem.upper()   # …and extract the name of the file to display the country code next.
                    print(f'{cc} error: {error_msg}')
            counter[status] += 1

    return counter

def download_many(
    cc_list: list[str],
    base_url: str,
    verbose: bool,
    concur_req: int
) -> Counter[DownloadStatus]:
    """
    download_many instantiates the supervisor coroutine object and passes it to the 
    event loop with asyncio.run, collecting the counter supervisor returns when
    the event loop ends.
    """
    coro = supervisor(cc_list, base_url, verbose, concur_req)
    counts = asyncio.run(coro)

    return counts

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
# end::FLAGS2_ASYNCIO_START[]