import asyncio
import itertools
import time
import math

async def spin(msg: str) -> None:  # We don’t need the Event argument that was used to signal that
                                   # `slow` had completed its job like in thread or process versions
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)  # Use `await asyncio.sleep(.1)` instead of `time.sleep(.1)`, to pause without blocking other coroutines
        except asyncio.CancelledError:  # `asyncio.CancelledError` is raised when the cancel method is called on the `Task` controlling this coroutine
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def slow() -> int:
    # await asyncio.sleep(3)  # also uses `await asyncio.sleep` instead of `time.sleep` to pause without blocking other coroutines
    # time.sleep(3)  # experiment: with time.sleep, we will not see the spin at all
    await is_prime(5_000_111_000_222_021)
    return 42

async def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
        if i % 100_000 == 1:
            await asyncio.sleep(0)
    print(f"\n{n} is a prime")
    return True

async def supervisor() -> int:  # Native coroutines are defined with async def
    spinner = asyncio.create_task(spin('spinning!'))  # `asyncio.create_task` schedules the eventual execution
                                                      # of `spin`, immediately returning an instance of `asyncio.Task`
    print(f'spinner object: {spinner}')  # should print an `asyncio.Task` object
    result = await slow()  # The `await` keyword calls `slow`, blocking supervisor until `slow` returns
    spinner.cancel()  # The `Task.cancel` method raises a `CancelledError` exception inside the `spin` coroutine
    return result

def main() -> None:  # since we are running in the jupyter notebook, which is already an async context, 
                           # we have to make main an async function and await for it
    result = asyncio.run(supervisor())
    # The `asyncio.run` function starts the event loop to drive 
    # the coroutine that will eventually set the other coroutines 
    # in motion. The main function will stay blocked until supervisor returns
    # `supervisor`'s return value will be the return value of `asyncio.run`.
    print(f'-- Answer: {result}')

if __name__ == '__main__':
    main()