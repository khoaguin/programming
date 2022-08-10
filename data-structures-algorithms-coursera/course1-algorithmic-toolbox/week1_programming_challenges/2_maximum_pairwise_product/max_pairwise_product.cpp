// Input: A sequence of non-negative integers.
// Output: The maximum value that can be obtained by multiplying 
// two different elements from the sequence.

#include <iostream>
#include <vector>
#include <algorithm>

// Naive solution: loop through all pairs (O(n^2))
long long MaxPairwiseProductNaive(const std::vector<int>& numbers) {
    long long max_product = 0;
    int n = numbers.size();
    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            if ((long long) numbers[first] * numbers[second] > max_product) {
                max_product = (long long) numbers[first] * numbers[second];
            }
        }
    }
    return max_product;
}

// Better solution: finding 2 maximal numbers in the sequence (O(n))
// Incorrect implementation (in the step of finding the 2nd max number)
long long MaxPairwiseProductBetter(const std::vector<int>& numbers) {
    long long max_product = 0;
    int n = numbers.size();
    // Find the first maximum number
    int first_max = -1;
    for (int i=0; i<n; ++i) {
        if (numbers[i] > first_max) {
            first_max = numbers[i];
        }
    }
    // Find the second maximum number
    int second_max = -1;
    for (int i=0; i<n; ++i) {
        if (numbers[i] > second_max && numbers[i] != first_max) {
            second_max = numbers[i];
        }
    }
    
    return (long long) first_max * second_max;
}

// Better solution: finding 2 maximal numbers in the sequence (O(n))
long long MaxPairwiseProductFast(const std::vector<int>& numbers) {
    long long max_product = 0;
    int n = numbers.size();
    // Find the index of the first maximum number
    int max_index1 = -1;
    for (int i = 0; i < n; ++i) {
        if (max_index1 == -1 || numbers[i] > numbers[max_index1]) {
            max_index1 = i;
        }
    }
    // Find the index of the second maximum number
    int max_index2 = -1;
    for (int j = 0; j < n; ++j) {
        if (j != max_index1 && ((max_index2 == -1) || numbers[j] > numbers[max_index2])) {
            max_index2 = j;
        }
    }
    // std::cout << numbers[max_index1] << ' ' << numbers[max_index2] << '\n';
    return (long long) numbers[max_index1] * numbers[max_index2];
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProductFast(numbers) << "\n";
    return 0;
}