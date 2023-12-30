import asyncio
import itertools


async def spin(
    msg: str,
) -> None:  # no need for Event to signal that slow has done its job
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(
                0.1
            )  # use asyncio.sleep instead of time.sleep() to pause without blocking other coroutines
        except (
            asyncio.CancelledError
        ):  # this is called when the cancel method is called on the Task controlling this coroutine
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")
    print("END OF SPIN")


async def slow() -> int:
    await asyncio.sleep(3)  # use asyncio.sleep instead of time.sleep
    return 42


def main() -> None:  # main is the only function. others are coroutines
    result = asyncio.run(
        supervisor()
    )  # starts the event loop to drive the coroutine that will eventually set the other coroutines in motion
    print(f"Answer: {result}")


async def supervisor() -> int:  # Native coroutines are defined with async def
    spinner: asyncio.Task = asyncio.create_task(
        spin("thinking!")
    )  # schedules the eventual execution of spin, immediately returning an instance of asyncio.Task
    print(f"spinner object: {spinner}")
    result = await slow()  # calls slow(), block supervisor() until slow() returns
    spinner.cancel()  # raises a CancelledError exception
    return result


if __name__ == "__main__":
    main()
