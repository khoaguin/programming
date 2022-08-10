// Input: The first line of the input contains the number n of items 
// and the capacity W of a knapsack. The next n lines define the values 
// and weights of the items. The i-th line contains integers v_i and w_i — the
// value and the weight of i-th item, respectively.
// Output: the maximal value of fractions of items that fit into the knapsack. 
// The absolute value of the difference between the answer of your program and 
// the optimal value should be at most 1e−3. To ensure this, output your answer 
// with at least four digits after the decimal point (otherwise your answer, 
// while being computed correctly, can turn out to be wrong because of rounding issues).


#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using std::vector;

int most_expensive_index(vector<int> weights, vector<int> values) {
  // return the index of the most expensive item
  int max_index = 0;
  double max_value = -1;
  for (int i = 0; i < weights.size(); ++i) {
    double cost = (double) values[i] / weights[i];
    if (cost > max_value) {
      max_index = i;
      max_value = cost;
    }
  }
  return max_index;
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  // idea: get the item with maximum value each time until we run out of capacity
  //       or we have got all the items

  // base case
  if (capacity == 0 || weights.size() == 0) {
    return 0.0;
  }

  // recursive case
  // the index of the most expensive item
  // int m = std::max_element(values.begin(), values.end()) - values.begin();
  int m = most_expensive_index(weights, values);
  int amount_taken = std::min(weights[m], capacity);
  double value = (double) values[m] / weights[m];
  value = (double) value * amount_taken;
  // std::cout << std::fixed << value << " \n";
  // remove the taken items
  capacity = capacity - amount_taken;
  weights.erase(weights.begin() + m);
  values.erase(values.begin() + m);

  return value + get_optimal_value(capacity, weights, values);
}

int main() {
  // get user input
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  std::cout << std::fixed;
  std::cout << std::setprecision(4);
  double optimal_value = get_optimal_value(capacity, weights, values);
  std::cout << optimal_value << std::endl;

  return 0;
}
