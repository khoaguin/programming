#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        nums[:] = sorted(s)
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two-pointer solution
        """
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow + 1] = nums[fast]
                slow += 1
                fast += 1
        return slow + 1

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Using .pop() to remove elements
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(s.removeDuplicates([1, 1, 2]))


# @lc code=end
