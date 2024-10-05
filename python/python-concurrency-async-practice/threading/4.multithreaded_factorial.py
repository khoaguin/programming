import threading


def partial_factorial(start: int, end: int, result: list, result_lock):
    partial = 1
    for i in range(start, end + 1):
        partial *= i
    with result_lock:
        result[0] *= partial


def calculate_factorial(n):
    mid = n // 2
    result_lock = threading.Lock()
    result = [1]

    thread1 = threading.Thread(
        target=partial_factorial, 
        args=(1, mid, result, result_lock)
    )
    thread2 = threading.Thread(
        target=partial_factorial, 
        args=(mid+1, n, result, result_lock)
    )
    
    print(f"\nCalculating factorial of {n} using two threads")

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

    print(f"Factorial of {n} is {result[0]}")

n = 5
calculate_factorial(n)