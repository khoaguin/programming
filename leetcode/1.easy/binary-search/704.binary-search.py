#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Recursive solution
            Runtime: O(log n) - beats 95.46 % of python3 submissions
            Mem: beats 15.51 % of python3 submissions (18 MB)
        """

        def binary_search(
            nums: List[int], target: int, low_idx: int, high_idx: int
        ) -> int:
            # important case to reduce runtime
            if len(nums) == 1 and nums[0] == target:
                return 0

            mid_idx = low_idx + (high_idx - low_idx) // 2

            print(f"{low_idx = }, {high_idx = }, {mid_idx = }")

            if low_idx > high_idx:
                return -1
            if target == nums[mid_idx]:
                return mid_idx
            elif target < nums[mid_idx]:
                # search the lower half of the list
                return binary_search(
                    nums=nums, target=target, low_idx=low_idx, high_idx=mid_idx - 1
                )
            else:
                # search the upper half of the list
                return binary_search(
                    nums=nums, target=target, low_idx=mid_idx + 1, high_idx=high_idx
                )

        return binary_search(nums, target, 0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    # print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    # print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=12))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12, 13], target=9))
    # print(s.search(nums=[5], target=5))
    # print(s.search(nums=[2, 5], target=5))


# @lc code=end
