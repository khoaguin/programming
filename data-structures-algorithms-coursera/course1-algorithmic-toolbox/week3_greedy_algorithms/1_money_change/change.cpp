// Task: The goal in this problem is to find the minimum number of 
//  coins needed to change the input value (an integer) into coins 
//  with denominations 1, 5, and 10.
// Input Format: The input consists of a single integer m (1 <= m <= 10^3).
// Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m


#include <iostream>


int get_change(int m) {
  //write your code here
  return m / 10 + (m % 10) / 5 + m % 5;  
}


int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
