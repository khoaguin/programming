# Input: A sequence of non-negative integers.
# Output: The maximum value that can be obtained by multiplying 
# two different elements from the sequence.

from typing import List

def max_pairwise_product(numbers: List) -> int:
    n = len(numbers)
    # find the index of the first maximum number
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
    # find the index of the second maximum number 
    max_index2 = -1
    for j in range(n):
        if (j != max_index1) and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j
    # print(max_index1, max_index2)
    
    return numbers[max_index1] * numbers[max_index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
