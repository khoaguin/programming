# Task: Given an integer n, find the last digit of the 
#        n-th Fibonacci number (that is, Fn mod 10)
# Input: A single integer n
# Output: The last digit of Fn
# Example Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current


if __name__ == '__main__':
    n = int(input())
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))