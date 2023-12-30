import asyncio
import itertools
import math
import time


async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    print("THIS WILL NEVER BE OUTPUT")


async def is_prime(n: int) -> bool:
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
    return True


async def supervisor(p: int) -> int:
    spinner = asyncio.create_task(
        spin("thinking!")
    )  # The spinner task is created, to eventually drive the execution of spin
    print(f"spinner object: {spinner}")  # The display shows the Task is “pending.”
    result = await is_prime(
        5_000_111_000_222_021
    )  # The await expression transfers control to the slow coroutine.
    spinner.cancel()  # Right after slow returns, the spinner task is cancelled
    return result


def main() -> None:
    p = 5_000_111_000_222_021
    result = asyncio.run(supervisor(p))
    print(f"{p} is a prime: {result}")


if __name__ == "__main__":
    main()
