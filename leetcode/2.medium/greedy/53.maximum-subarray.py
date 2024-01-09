#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Bruteforce solution:
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        res = float("-inf")
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                res = max(res, cur_sum)
        return res

    def maxSubArray(self, nums):
        """
        Recursive Solution: At each index i, we can either pick that element or not pick it.
            If we pick current element, then all future element must also be picked
                since our array needs to be contiguous.
            If we had picked any elements till now, we can either end further
                recursion at any time by returning sum formed till now or
                we can choose current element and recurse further. This denotes two choices
                of either choosing the subarray formed from 1st picked element
                till now or expanding the subarray by choosing current element respectively.
        Time Complexity : O(N^2), we are basically considering every subarray sum and choosing maximum of it.
        Space Complexity : O(N), for recursive space
        """

        def solve(i: int, must_pick: bool) -> int:
            if i >= len(nums):  # base case
                return 0 if must_pick else float("-inf")
            # recursive cases
            if must_pick:  # must_pick indicates that we  already formed a subarray
                # If must_pick is True, there are two choices:
                # Pick the current element (nums[i]) and add it to the ongoing subarray, then recurse with the next element (i + 1), maintaining must_pick as True.
                # End the current subarray here, which is represented by returning 0, signifying no further elements are added to the subarray.
                return max(nums[i] + solve(i + 1, True), 0)
            else:
                # If must_pick is False, the choices expand:
                # Either start a new subarray with the current element (nums[i]) and continue with the next elements (i + 1), setting must_pick to True.
                # Or skip the current element, continuing the recursion with i + 1 without changing the must_pick status.
                return max(nums[i] + solve(i + 1, True), solve(i + 1, False))

        return solve(0, False)


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))

# @lc code=end
