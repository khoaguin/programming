// Task: Given an integer n, find the last digit of the 
//        n-th Fibonacci number (that is, Fn mod 10)
// Input: A single integer n
// Output: The last digit of Fn
// Example Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#include <iostream>
#include <cassert>


// Slow solution because as i grows, the i-th iteration
// will compute the sum of longer and longer numberes.
// Also, for large n (e.g. 1000), F_1000 will not fit in
// the standard C++ int type.
int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}


// Only store the last digit of the i-th Fibonacci number, not
// the whole number itself.
int get_fibonacci_last_digit_fast(int n) {
    if (n <= 1)
        return n;

    int f[n+1] = {0, 1}; 
    for (int i = 2; i < n + 1; ++i) {
        // only store the last digit of the sum. This works because
        // e.g. (29 + 33) % 10 = (9 + 3) % 10
        f[i] = (f[i-1] + f[i-2]) % 10;
    }
    return f[n];
}


// Only store the last digit of the i-th Fibonacci number, not
// the whole number itself.
int get_fibonacci_last_digit_fast_2(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current = 1;
    for (int i = 0; i < n - 1; ++i) {
        int temp_previous = previous % 10;
        previous = current % 10;
        current = (temp_previous + current) % 10;
    }
    return current;
}

// only test the first 30 Fibonacci sequences
void test_solution() {
    for (int n = 0; n < 30; ++n)
        assert(get_fibonacci_last_digit_fast_2(n) == get_fibonacci_last_digit_naive(n));
    std::cout << "Test passed!" << "\n";
}


int main() {
    int n;
    std::cin >> n;
    // test_solution();
    // std::cout << get_fibonacci_last_digit_naive(n) << '\n';
    std::cout << get_fibonacci_last_digit_fast_2(n) << '\n';
}