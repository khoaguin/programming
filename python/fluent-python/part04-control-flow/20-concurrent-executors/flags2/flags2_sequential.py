#!/usr/bin/env python3

"""Download flags of countries (with error handling).

Sequential version

Sample run::

    $ python3 flags2_sequential.py -s DELAY b
    DELAY site: http://localhost:8002/flags
    Searching for 26 flags: from BA to BZ
    1 concurrent connection will be used.
    --------------------
    17 flags downloaded.
    9 not found.
    Elapsed time: 13.36s

"""

# tag::FLAGS2_BASIC_HTTP_FUNCTIONS[]
from collections import Counter
from http import HTTPStatus

import httpx
import tqdm  # type: ignore

from flags2_common import main, save_flag, DownloadStatus  # <2>

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1

def get_flag(base_url: str, cc: str) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=3.1, follow_redirects=True)
    resp.raise_for_status()  # Raises HTTPStetusError if the HTTP status code is not in range(200, 300).

    return resp.content

def download_one(cc: str, base_url: str, verbose: bool = False) -> DownloadStatus:
    try:
        image = get_flag(base_url, cc)
    except httpx.HTTPStatusError as exc:  # download_one catches HTTPStatusError to handle HTTP code 404 specifically
        res = exc.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND  # by setting its local status to DownloadStatus.NOT_FOUND
            msg = f'not found: {res.url}'
        else:
            raise  # Any other HTTPStatusError exception is re-raised to propagate to the caller.
    else:
        save_flag(image, f'{cc}.gif')
        status = DownloadStatus.OK
        msg = 'OK'

    if verbose:
        print(cc, msg)

    return status
# end::FLAGS2_BASIC_HTTP_FUNCTIONS[]

# tag::FLAGS2_DOWNLOAD_MANY_SEQUENTIAL[]
def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  _unused_concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()  # tally the download outcomes
    cc_iter = sorted(cc_list)
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)
    for cc in cc_iter:
        try:
            status = download_one(cc, base_url, verbose)  # Make successive calls to download_one
        except httpx.HTTPStatusError as exc:  # HTTP status code exceptions raised by get_flag
            error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
            error_msg = error_msg.format(resp=exc.response)
        except httpx.RequestError as exc:  # Another network-related exception
            error_msg = f'{exc} {type(exc)}'.strip()
        except KeyboardInterrupt:  # Exit the loop if the user hits Ctrl-C
            break
        else:  # If no exception escaped download_one, clear the error message
            error_msg = ''

        if error_msg:
            status = DownloadStatus.ERROR  # If there was an error, set the local status accordingly
        counter[status] += 1           # Increment the counter for that status
        if verbose and error_msg:      # In verbose mode, display the error message for the current country code, if any
            print(f'{cc} error: {error_msg}')

    return counter  # Return `counter` so that `main` can display the numbers in the final report.
# end::FLAGS2_DOWNLOAD_MANY_SEQUENTIAL[]

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)