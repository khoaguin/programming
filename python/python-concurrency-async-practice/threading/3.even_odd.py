# Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50. 

from threading import Thread

numbers = list(range(30, 51))
even_nums = []
odd_nums = []

def even_num(numbers: list[int], even_nums: list):
    for i in numbers:
        if i % 2 == 0:
            print(f"even number from even thread: {i}")
            even_nums.append(i)

def odd_num(numbers: list[int], odd_nums: list):
    for i in numbers:
        if i % 2 != 0:
            print(f"odd number from odd thread: {i}")
            odd_nums.append(i)
        
even_thread = Thread(target=even_num, args=(numbers, even_nums))
odd_thread = Thread(target=odd_num, args=(numbers, odd_nums))
# Start the threads
even_thread.start()
odd_thread.start()
# Wait for the threads to complete
odd_thread.join()
even_thread.join()

print(f"{even_nums = }")
print(f"{odd_nums =}")