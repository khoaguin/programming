import asyncio
import time

async def fetch_data(url):
    print(f"Start fetching data from {url}")
    # Simulate a network request
    await asyncio.sleep(2)
    print(f"Finished fetching data from {url}")
    return f"Data from {url}"

async def main():
    start_time = time.time()

    # List of URLs to fetch
    urls = [
        "https://api.example.com/data1",
        "https://api.example.com/data2",
        "https://api.example.com/data3",
    ]

    # Create tasks for each URL
    tasks = [fetch_data(url) for url in urls]

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    print("\nResults:")
    for result in results:
        print(result)
    
    # will be 2 secs instead of 6 secs thanks to async
    print(f"\nTotal time taken: {total_time:.2f} seconds")

# Run the async program
asyncio.run(main())