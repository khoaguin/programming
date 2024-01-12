#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


from functools import lru_cache

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

        def f(i: int, must_pick: bool) -> int:
            if i >= len(nums):  # base case
                return 0 if must_pick else float("-inf")
            # recursive cases
            if must_pick:  # must_pick indicates that we  already formed a subarray
                # If must_pick is True, there are two choices:
                # Pick the current element (nums[i]) and add it to the ongoing subarray, then recurse with the next element (i + 1), maintaining must_pick as True.
                # End the current subarray here, which is represented by returning 0, signifying no further elements are added to the subarray.
                return max(nums[i] + f(i + 1, True), 0)
            else:
                # If must_pick is False, there are also 2 choices:
                # Either start a new subarray with the current element (nums[i]) and continue with the next elements (i + 1), setting must_pick to True.
                # Or skip the current element, continuing the recursion with i + 1 without changing the must_pick status.
                return max(nums[i] + f(i + 1, True), f(i + 1, False))

        return f(0, False)

    def maxSubArray(self, nums):
        """
        DP with Memoization solution using @cache
        """

        @lru_cache(maxsize=16)
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else float("-inf")
            return max(
                nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False)
            )

        return solve(0, False)

    def maxSubArray(self, nums):
        """
        Manual DP with Memoization solution: Built upon the the recursion approach, where
            we call the function `f` a lot of times (draw the recursion tree to see).
            Now, let's make a dp list for memoization where `dp[mustPick][i]` denotes the
                maximum sum subarray starting from `i` and `mustPick` denotes wheter the current
                element must be picked or not.
        Time Complexity: O(n)
        Space Complexity: Worst case O(n)
        """
        dp: List[List[int]] = [
            [float("-inf")] * len(nums) for i in (0, 1)
        ]  # 0 is False, 1 is True

        def f(i: int, must_pick: bool, dp: List[List[int]]) -> int:
            if i >= len(nums):  # base case
                return 0 if must_pick else float("-inf")

            if dp[must_pick][i] != float(
                "-inf"
            ):  # already computed: just return the value
                return dp[must_pick][i]

            if must_pick:
                dp[must_pick][i] = max(nums[i] + f(i + 1, True, dp), 0)
            else:
                dp[must_pick][i] = max(
                    nums[i] + f(i + 1, True, dp), f(i + 1, False, dp)
                )

            return dp[must_pick][i]

        return f(0, False, dp)

    def maxSubArray(self, nums):
        """
        DP with Tabulation
            Use dp[1][i] to denote the maximum subarray ending at i
            Use dp[0][i] to denote the maximum subarray sumed upto i
            At each index:
                - We update dp[1][i] as max between either only choosing
                    current element `nums[i]` (new subarray) or extending from previous
                    subarray and also the current element: `dp[1][i-1] + nums[i]`
                - We update dp[0][i] as max between either the sum of subarray until
                    the last element (dp[0][i-1]) or until the current element (dp[1][i])
            Finally, we return the last element of dp[0]: dp[0][-1]
        Time Complexity: O(n)
        Space Complexity: O(2n) = O(n)
        """
        dp = [[0] * len(nums) for i in (0, 1)]
        dp[1][0], dp[0][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i - 1])
            dp[0][i] = max(dp[0][i - 1], dp[1][i])
        return dp[0][-1]

    def maxSubArray(self, nums):
        """
        Optimized DP with Tabulation:
            The `dp` list is now 1D, and at each index, we make `dp[i]` as the maximum
            between the current number nums[i], or the sum of num[i] and dp[i-1]
            Finally we return the maximum of `dp`
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dp = [*nums]  # copy nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)

    def maxSubArray(self, nums):
        """
        Kadane's algorithm:
            Observing the optimized DP with tabulation, we can see that we do not need
            to keep the `dp` list, but only the current max and the max value until now.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        cur_max, max_till_now = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i] + cur_max)
            max_till_now = max(cur_max, max_till_now)
        return max_till_now


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))

# @lc code=end
