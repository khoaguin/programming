#!/usr/bin/env python3

"""Download flags of countries (with error handling).

ThreadPool version

Sample run::

    $ python3 flags2_threadpool.py -s ERROR -e
    ERROR site: http://localhost:8003/flags
    Searching for 676 flags: from AA to ZZ
    30 concurrent connections will be used.
    --------------------
    150 flags downloaded.
    361 not found.
    165 errors.
    Elapsed time: 7.46s

"""

# tag::FLAGS2_THREADPOOL[]
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx
import tqdm  # type: ignore

from flags2_common import main, DownloadStatus
from flags2_sequential import download_one

DEFAULT_CONCUR_REQ = 30  # maximum number of concurrent requests, implemented as the size of the thread pool;
MAX_CONCUR_REQ = 1000  # the maximum number of concurrent requests regardless 
                       # of the number of flags to download or the -m/--max_req command-line option


def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    with ThreadPoolExecutor(max_workers=concur_req) as executor:  # Create the executor with max_workers set to concur_req
        to_do_map = {}  # map each Future instance—representing one download—with the
                        # respective country code for error reporting
        for cc in sorted(cc_list):  # Iterate over the list of country codes in alphabetical order.
                                    # The order of the results will mostly depend on the timing of the HTTP responses
                                    # but if the size of the thread pool (given by concur_req) is much smaller than
                                    # len(cc_list), you may notice the downloads batched alphabetically
            future = executor.submit(download_one, cc,
                                     base_url, verbose)  # Each call to executor.submit schedules the
                                                         # execution of one callable and returns a Future instance
            to_do_map[future] = cc  # Store the future and the country code in the dict.
        done_iter = as_completed(to_do_map)  # futures.as_completed returns an iterator that yields futures as each task is done.
        if not verbose:
            done_iter = tqdm.tqdm(done_iter, total=len(cc_list))  # Wrap done_iter with tqdm.tqdm to show a progress bar.
        for future in done_iter:  # Iterate over the futures as they are completed
            try:
                status = future.result()  # Calling the result method on a future either returns the value returned by the
                                          # callable, or raises whatever exception was caught when the callable was executed.
            except httpx.HTTPStatusError as exc:  # Handle the potential exceptions;
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=exc.response)
            except httpx.RequestError as exc:
                error_msg = f'{exc} {type(exc)}'.strip()
            except KeyboardInterrupt:
                break
            else:
                error_msg = ''

            if error_msg:
                status = DownloadStatus.ERROR
            counter[status] += 1
            if verbose and error_msg:
                cc = to_do_map[future]  # To provide context for the error message, retrieve the
                                        # country code from the to_do_map using the current future as key
                print(f'{cc} error: {error_msg}')

    return counter


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
# end::FLAGS2_THREADPOOL[]