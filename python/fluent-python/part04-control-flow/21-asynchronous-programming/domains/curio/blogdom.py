#!/usr/bin/env python3
from curio import run, TaskGroup
import curio
from keyword import kwlist

MAX_KEYWORD_LEN = 4


async def probe(domain: str) -> tuple[str, bool]:  # probe doesn’t need to get the event loop
    try:
        # getaddrinfo is a top-level function of curio.socket,
        # not a method of a loop object—as it is in asyncio
        await curio.socket.getaddrinfo(domain, None)
    except curio.socket.gaierror:
        return (domain, False)
    return (domain, True)


async def main() -> None:
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f'{name}.dev'.lower() for name in names)
    
    # A TaskGroup is a core concept in Curio, to monitor and control several
    # coroutines, and to make sure they are all executed and cleaned up
    async with TaskGroup() as group:
        for domain in domains:
            await group.spawn(probe, domain)  # `TaskGroup.spawn` is how you start a coroutine
        # Iterating with `async for` over a `TaskGroup` yields `Task` instances as each is completed
        async for task in group:
            domain, found = task.result
            mark = '+' if found else ' '
            print(f'{mark} {domain}')


if __name__ == '__main__':
    run(main())  # Curio pioneered this sensible way to start an asynchronous program in Python
