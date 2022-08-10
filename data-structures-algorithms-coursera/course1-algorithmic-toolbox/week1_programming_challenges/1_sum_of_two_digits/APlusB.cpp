// Input format: Integers a and b on the same line (separated by a space).
// Output format: The sum of a and b.

#include <iostream>

int sum_of_two_digits(int x, int y) {
    return x + y;
}

int main() {
    int x = 0;
    int y = 0;
    std::cin >> x;
    std::cin >> y;
    std::cout << sum_of_two_digits(x, y);
    return 0;
}