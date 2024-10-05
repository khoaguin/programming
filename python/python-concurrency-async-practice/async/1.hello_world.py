# Write a Python program that creates three asynchronous functions and 
# displays their respective names with different delays
import asyncio

async def display_name_with_delay(name, delay):
    await asyncio.sleep(delay)
    print(name)

async def main():
    tasks = [
        display_name_with_delay("Asyn. function-3", 3),
        display_name_with_delay("Asyn. function-2", 2),
        display_name_with_delay("Asyn. function-1", 1),
    ]    
    await asyncio.gather(*tasks)

# Run the event loop
asyncio.run(main())
