# Input: The first two lines of the input contain an integer n and a sequence 
#        a0 < a1 < · · · < an − 1 of n distinct positive integers in increasing order. 
#        The next two line contain an integer k and k positive integers b0, b1, . . . , bk − 1.
# Output: For all i from 0 to k − 1, output an index 0 ≤ j ≤ n − 1 of the first occurrence of 
#         bi (i.e., aj = bi) or −1 if there is no such index


def binary_search(keys, query):
    high = len(keys) - 1
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        if keys[mid] == query:
            while (keys[mid-1] == query):
                mid = mid - 1
            return mid
        elif keys[mid] > query:
            high = mid - 1
        else: 
            low = mid + 1
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')