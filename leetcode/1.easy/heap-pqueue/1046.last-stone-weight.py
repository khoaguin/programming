#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#


import heapq

# @lc code=start
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Using a max heap
        """
        heapq._heapify_max(stones)
        while len(stones) > 1:
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            if x != y:
                # add back the
                y -= x
                stones.append(y)
                heapq._siftdown_max(stones, 0, len(stones) - 1)

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Using a negated min heap
        Runtime Complexity: O(n log n)
        Space Complexity: O(n) to store the heap
        """
        negated_stones = [-stone for stone in stones]
        heapq.heapify(negated_stones)  # O(n)

        while len(negated_stones) > 1:  # total O(n log n)
            y = -1 * heapq.heappop(negated_stones)  # O(log n)
            x = -1 * heapq.heappop(negated_stones)  # O(log n)
            if x != y:
                z = y - x
                heapq.heappush(negated_stones, -z)  # O(log n)

        return -1 * negated_stones[0] if len(negated_stones) == 1 else 0


s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
# @lc code=end
