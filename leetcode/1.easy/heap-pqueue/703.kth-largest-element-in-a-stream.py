#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

import heapq
from typing import List


# @lc code=start
class KthLargest:
    """
    Approach: Using a min heap
    Only keep k elements in the heap, and the kth largest will be at the root
    Runtime Complexity: O(n log k) for initialization and O(log k) for each addition
        Beats 73.9% of users with Python3
    Space Complexity: O(k) since the heap size is always maintained at a maximum of k elements.
        Beats 6.21% of users with Python3
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Runtime Complexity: O(n log k) where n = len(nums), since
            heapify takes O(n),
            _keep_only_k_elems takes O(log k * (n-k)),
            Hence, overall runtime is O(n + log k * (n-k)) = O(n log k)
        Space Complexity: O(k)
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        self._keep_only_k_elems()

    def _keep_only_k_elems(self):
        """
        Each heappop operation takes O(log k) time, and we might do n-k times
        Hence, runtime complexity is O(log k * (n-k))
        """
        while len(self.heap) > self.k:
            # Pop the smallest item from the heap
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        heappush takes O(log k), where k is the number of nodes in the heap
        heappop also takes O(log k)
        Hence overall runtime is O(log k)
        """

        if len(self.heap) < self.k or val > self.heap[0]:
            heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
assert obj.add(3) == 4
assert obj.add(5) == 5
assert obj.add(10) == 5
assert obj.add(9) == 8
assert obj.add(4) == 8

obj = KthLargest(1, [])
assert obj.add(-3) == -3
assert obj.add(-2) == -2
assert obj.add(-4) == -2
assert obj.add(0) == 0
assert obj.add(4) == 4

# @lc code=end
