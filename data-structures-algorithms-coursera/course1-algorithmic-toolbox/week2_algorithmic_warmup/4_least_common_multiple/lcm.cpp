// Input: The two integers a and a are given in the same line separated by space
// Output: The least common multiple of a and b

#include <iostream>
#include <cassert>


long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l) {
    if (l % a == 0 && l % b == 0)
      return l;
  }
  return (long long) a * b;
}


int gcd(int a, int b) {
  if (b == 0) {
    return a;
  }
  int c = a % b;

  return gcd(b, c);
}


long long lcm_fast(int a, int b) {
  int m = gcd(a, b);
  int c = a / m;
  
  return (long long) c * b;
}


void test_solution() {
  while (true) {
    int a = rand() % 1000 + 2;
    int b = rand() % 1000 + 2;
    std::cout << a << ' ' << b << '\n';
    assert(lcm_naive(a, b) == lcm_fast(a, b));
  }
}

int main() {
  int a, b;
  std::cin >> a >> b;
  // std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_fast(a, b) << std::endl;
  
  // test_solution(); 

  return 0;
}
