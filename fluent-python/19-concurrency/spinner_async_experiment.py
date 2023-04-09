import asyncio
import itertools
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


async def slow() -> int:
    time.sleep(
        3
    )  # time.sleep(3) blocks for 3 seconds; nothing else can happen in the program, because the main thread is blocked—and it is the only thread.
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(
        spin("thinking!")
    )  # The spinner task is created, to eventually drive the execution of spin
    print(f"spinner object: {spinner}")  # The display shows the Task is “pending.”
    result = (
        await slow()
    )  # The await expression transfers control to the slow coroutine.
    spinner.cancel()  # Right after slow returns, the spinner task is cancelled
    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
