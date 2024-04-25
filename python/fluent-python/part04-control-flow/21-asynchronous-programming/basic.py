import asyncio

async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # Pause execution for 1 second
    print("End")

async def other_task():
    print("Doing other task")
    await asyncio.sleep(0.5)  # Pause execution for 0.5 seconds
    print("Other task complete")

async def main():
    task1 = my_coroutine()  # Start my_coroutine
    task2 = other_task()    # Start other_task
    await asyncio.gather(task1, task2)  # Wait for both tasks to complete

asyncio.run(main())