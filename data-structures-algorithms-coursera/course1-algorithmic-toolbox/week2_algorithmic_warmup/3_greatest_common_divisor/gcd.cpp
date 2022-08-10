// Input: The two integers a, b are given in the same line separated by space.
// Output: The greatest common divisor of a and b

#include <iostream>


int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}


int gcd_euclid(int a, int b) {
  if (b == 0) {
    return a;
  }
  int a_prime = a % b;
  return gcd_euclid(b, a_prime);
}


void stress_test() {
  while (true) {
    int a = rand() % 10000 + 2;
    int b = rand() % 10000 + 2;
    std::cout << a << ' ' << b << "\n";
    int res1 = gcd_naive(a, b);
    int res2 = gcd_euclid(a, b);
    if (res1 != res2) {
      std::cout << "Wrong answer: " << res1 << ' ' << res2 << "\n";
      break;
    }
    else {
      std::cout << "OK\n";
    }
  }
}


int main() {
  int a, b;
  std::cin >> a >> b;
  // stress_test();
  std::cout << gcd_euclid(a, b) << std::endl;
  return 0;
}
