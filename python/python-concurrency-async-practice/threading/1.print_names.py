# Write a Python program to create multiple threads and print their names. 


from threading import Thread
import threading

def print_current_thread_name():
    print(f"current thread: {threading.current_thread().name}")

threads = []

# Create multiple threads and start printing their names
for i in range(5):
    thread = Thread(target=print_current_thread_name)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads: thread.join()
