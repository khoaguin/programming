#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        My Solution: Using a hash table
        """
        print("a")
        value_idx = dict()
        for i, v in enumerate(nums):
            if v not in value_idx:
                value_idx[v] = [i]
            else:
                value_idx[v].append(i)

        for i, v in enumerate(nums):
            # find the index of target - v
            compliment = target - v
            if compliment in value_idx:
                if compliment != v:
                    return list(set([i, *value_idx[compliment]]))
                if compliment == v and len(value_idx[compliment]) == 2:
                    return value_idx[compliment]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two-pass Hash Table
            Time complexity: O(N);
            Space Complexity: O(N);
        """
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        One-pass Hash Table
            Time complexity: O(N);
            Space Complexity: O(N);
        """
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 3], 6) == [0, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]

# @lc code=end
