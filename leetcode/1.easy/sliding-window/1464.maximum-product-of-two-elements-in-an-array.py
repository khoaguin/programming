#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Brute-force
        """
        max_prod = 0
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i != j:
                    max_prod = max(max_prod, (nums[i] - 1) * (nums[j] - 1))
        return max_prod

    def maxProduct(self, nums: List[int]) -> int:
        """
        Keep track of 2 biggest numbers
        """
        first, sec = 0, 0
        for n in nums:
            if n > first:
                first, sec = n, first
            elif n > sec:
                first, sec = first, n
        return (first - 1) * (sec - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([3, 4, 5, 2]))
    print(s.maxProduct([1, 5, 4, 5]))
    print(s.maxProduct([3, 7]))

# @lc code=end
