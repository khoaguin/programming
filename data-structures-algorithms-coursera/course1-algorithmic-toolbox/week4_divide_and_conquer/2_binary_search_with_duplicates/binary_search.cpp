// Input: The first two lines of the input contain an integer n and a sequence 
//        a0 < a1 < · · · < an − 1 of n distinct positive integers in increasing order. 
//        The next two line contain an integer k and k positive integers b0, b1, . . . , bk − 1.
// Output: For all i from 0 to k − 1, output an index 0 ≤ j ≤ n − 1 of the first occurrence of 
//         bi (i.e., aj = bi) or −1 if there is no such index

#include <iostream>
#include <cassert>
#include <vector>
#include <cmath>
#include <algorithm>

using std::vector;

int binary_search(const vector<int> &a, int x, int low, int high) {
  int mid = low + floor((high - low) / 2);
  // std::cout << "low = " << low << " high = " << high << ' ';
  // std::cout << "mid = " << mid << '\n';
  // base case
  if (high < low)  {
    return -1;
  }
  if (a[mid] == x) {
    // find the minimal index (first occurence)
    while (a[mid - 1] == x) {
      mid = mid - 1;
    }
    return mid;
  }
  // recursive case
  else if (a[mid] < x) {
    return binary_search(a, x, mid + 1, high);
  }
  else {
    return binary_search(a, x, low, mid - 1);
  }
}

// Iterative solution
int binary_search_iterative(const vector<int> &a, int x) {
  int low = 0;
  int high = (int) a.size() - 1;
  while (low <= high) {
    int mid = low + floor((high - low) / 2);
    if (a[mid] == x) {
      while (a[mid - 1] == x) {
        mid = mid - 1;
      }
      return mid;
    } else if (a[mid] > x) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return -1;
}

int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

void stress_test() {
  while (true) {
    int n = rand() % 20 + 2;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); ++i) {
      a[i] = rand() % 20 + 2;
    }
    std::sort(a.begin(), a.end());

    std::cout << '\n';
    int k = rand() % 20 + 5;
    // assert (binary_search(a, k, 0, (int) a.size()) == linear_search(a, k));
    int res1 = linear_search(a, k);
    int res2 = binary_search(a, k, 0, (int) a.size() - 1);
    int res3 = binary_search_iterative(a, k);
    if (res1 != res3) {
        std::cout << "Wrong answer" << '\n';
        for (size_t i = 0; i < a.size(); ++i) {
          std::cout << a[i] << ", ";
        }
        std::cout << "\nk = " << k << "\n";
        std::cout << "linear search = " << res1 << "; bin search = " << res3 << '\n';
        break;
    }
    else {
        std::cout << "OK\n";
    }
  }
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  int m;
  std::cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    std::cin >> b[i];
  }
  int low = 0;
  int high = (int) a.size() - 1;
  for (int i = 0; i < m; ++i) {
    std::cout << binary_search_iterative(a, b[i]) << ' ';
  }

  // manual test for some special cases
  // vector<int> a{2};
  // std::cout << linear_search(a, -1) << '\n';
  // std::cout << binary_search(a, -1, 0, (int) a.size() - 1) << ' ';

  // stress_test();

}

