#!/usr/bin/env python3

"""Download flags of top 20 countries by population

asyncio + aiottp version

Sample run::

    $ python3 flags_asyncio.py
    EG VN IN TR RU ID US DE CN MX JP BD NG ET FR BR PH PK CD IR
    20 flags downloaded in 1.07s
"""
# tag::FLAGS_ASYNCIO_TOP[]
import asyncio

from httpx import AsyncClient

from flags import BASE_URL, save_flag, main


async def download_one(client: AsyncClient, cc: str):
    """
    `download_one` must be a native coroutine, so it can await on `get_flag` — 
    which does the HTTP request. Then it displays the code of the downloaded flag, and
    saves the image.
    """
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


async def get_flag(client: AsyncClient, cc: str) -> bytes:
    """
    get_flag needs to receive the AsyncClient to make the request.
    """
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1,
                follow_redirects=True)  # The get method of an httpx.AsyncClient 
                                        # instance returns a ClientResponse
                                        # object that is also an asynchronous context manager
    return resp.read()  # Network I/O operations are implemented as coroutine methods, so they are
                        # driven asynchronously by the asyncio event loop
# end::FLAGS_ASYNCIO_TOP[]

# tag::FLAGS_ASYNCIO_START[]
def download_many(cc_list: list[str]) -> int:    
    """
    This needs to be a plain function, not a coroutine so it can be passed
    to and called by the main function from the flags.py module
    """
    return asyncio.run(supervisor(cc_list))      # Execute the event loop driving the `supervisor(cc_list)` 
                                                # coroutine object until it returns.
                                                # This will block while the event loop runs.

async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:  # Asynchronous HTTP client operations in httpx are methods of AsyncClient,
                                        # which is also an asynchronous context manager: a context manager with asyn‐
                                        # chronous setup and teardown methods
        to_do = [download_one(client, cc)
                for cc in sorted(cc_list)]      # Build a list of coroutine objects by 
                                                # calling the `download_one` coroutine once for
                                                # each flag to be retrieved
        res = await asyncio.gather(*to_do)       # Wait for the asyncio.gather coroutine, which accepts 
                                                # one or more awaitable
                                                # arguments and waits for all of them to complete, 
                                                # returning a list of results for the
                                                # given awaitables in the order they were submitted.

    return len(res)                              # supervisor returns the length of the list returned by asyncio.gather

if __name__ == '__main__':
    main(download_many)
# end::FLAGS_ASYNCIO_START[]