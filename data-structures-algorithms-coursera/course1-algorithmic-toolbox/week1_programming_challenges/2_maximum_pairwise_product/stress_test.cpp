#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

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
long long MaxPairwiseProductBetter(const std::vector<int>& numbers) {
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
    std::cout << numbers[max_index1] << ' ' << numbers[max_index2] << '\n';
    return (long long) numbers[max_index1] * numbers[max_index2];
}

int main() {
    while (true) {
        int n = rand() % 10000 + 2;
        std::cout << n << "\n";
        std::vector<int> a;
        for (int i = 0; i < n; ++i) {
            a.push_back(rand() % 1000000);
        }
        for (int i = 0; i < n; ++i) {
            std::cout << a[i] << ' ';
        }
        std::cout << "\n";
        long long res1 = MaxPairwiseProductNaive(a);
        long long res2 = MaxPairwiseProductBetter(a);
        if (res1 != res2) {
            std::cout << "Wrong answer: " << res1 << ' ' << res2 << "\n";
            break;
        }
        else {
            std::cout << "OK\n";
        }
    }
    
    return 0;
}