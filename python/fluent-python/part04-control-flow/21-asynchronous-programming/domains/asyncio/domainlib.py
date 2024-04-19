import asyncio
import socket
from collections.abc import Iterable, AsyncIterator
from typing import NamedTuple, Optional


class Result(NamedTuple):  # NamedTuple makes the result from probe easier to read and debug.
    domain: str
    found: bool


OptionalLoop = Optional[asyncio.AbstractEventLoop]  # Type alias to avoid making the next line too long for a book listing


async def probe(domain: str, loop: OptionalLoop = None) -> Result:
    """
    probe now gets an optional loop argument, to avoid repeated calls to
    `get_running_loop` when this coroutine is driven by `multi_probe`.
    """
    if loop is None:
        loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return Result(domain, False)
    return Result(domain, True)


async def multi_probe(domains: Iterable[str]) -> AsyncIterator[Result]:
    """
    `multi_probe` is an asynchronous generator function that produces an asynchronous 
    generator object, which can be annotated as `AsyncIterator[SomeType]`.
    """
    loop = asyncio.get_running_loop()
    coros = [probe(domain, loop) for domain in domains]  # Build a list of probe coroutine 
                                                    # objects, each with a different domain
    for coro in asyncio.as_completed(coros):  # This is not `async for` because 
                                        # `asyncio.as_completed` is a classic generator.
        result = await coro  # Await on the coroutine object to retrieve the result
        yield result  # Yield result. This line makes `multi_probe` an asynchronous generator.
