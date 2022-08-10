# Input: An integer n >= 0
# Output: The Fibonnaci number at position n


def calc_fib(n):
    """
    Recursive solution. Very slow
    """
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def fibonacci_fast(n):
    """
    Iterative solution. Faster
    """
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


def test_solution():
    for n in range(20):
        assert fibonacci_fast(n) == calc_fib(n), \
            f"right solution: {calc_fib(n)}. Your solution: {fibonacci_fast(n)}"


if __name__ == '__main__':
    n = int(input())
    # test_solution()
    print(fibonacci_fast(n))
