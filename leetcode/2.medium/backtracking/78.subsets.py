#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtrack solution
        """

        def backtrack(
            res: List[List[int]], temp: List[int], nums: List[int], start: int
        ) -> None:
            """
            Args:
                res: stores the final result, a list of lists, each representing a subset.
                temp: is a temporary list that holds the current subset being constructed.
                nums: is the input list of integers.
                start: is an index indicating the starting point for processing nums.
            Runtime Complexity: O(2^N * N)
                There are 2^N possible subsets for a set of N elements.
                For each subset, the code makes a copy of the temp list, which takes O(N) time.
                Thus, the overall runtime complexity is O(2^N * N).

            Space Complexity: O(2^N * N)
                The space complexity is dominated by the space needed to store all the subsets.
                There are 2^N subsets, and in the worst case, a subset can have all N
                elements (e.g., the subset that is the entire set).
                Hence, the space complexity is O(2^N * N).

            Example code run: nums  = [1, 2, 3]
                i = 0: [], [1], [1, 2], [1, 2, 3]
                i = 1: [2], [2, 3]
                i = 2: [3]
            """
            # Note: only res.append(temp) will give a wrong answer as we are appending a
            # reference to the temp list, not a copy of its current state. As a result,
            # all appended lists in res actually reference the same list,
            # which ends up being empty at the end of the backtracking process due
            # to the temp.pop() calls.
            res.append(temp.copy())
            # print(f"{temp = }")
            for i in range(start, len(nums)):
                temp.append(
                    nums[i]
                )  # add the current element to temp forming a new subset
                # print(f"{i = }, {temp = }")
                backtrack(
                    res, temp, nums, i + 1
                )  # recursively explores further elements by incrementing start.
                temp.pop()

        # nums.sort()  # if we need to give answers in a particular order
        subsets = []
        backtrack(subsets, [], nums, 0)
        return subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative solution
        Time Complexity: O(2^N * N).
            Each number in nums doubles the number of subsets, and
            constructing each new subset can take up to O(N) time in the worst case.
        Space Complexity: O(2^N * N) for storing all subsets.
        """
        subsets = [[]]
        for num in nums:
            # print([curr + [num] for curr in subsets])
            subsets += [curr + [num] for curr in subsets]
        return subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Binary decision tree solution
        Reference: https://www.youtube.com/watch?v=REOH22Xwdkk
        For example, if nums = [1, 2], the decision tree will look like
                []        ------------> i = 0
              /    \
            [1]     []    ------------> i = 1
           /  \    /  \
        [1,2] [1] [2] []  ------------> i = 2
        Runtime Complexity: O(2^N * N)
            This is because there are two decisions (include or exclude) for each of the
            number (node) in the list nums.
            For each subset, the code makes a copy of the `subset` list, which takes O(N) time.
            Thus, the overall runtime complexity is O(2^N * N).
        Space Complexity: O(2^N * N) for storing all subsets, where the longest subset
            will have the length of N. We also need O(N) space for the recurive call stack, 
            but it's not a dominant term
        """
        res = []
        subset = []

        def bfs(index: int):
            # base case: we passed the leaf node
            if index >= len(nums):
                res.append(
                    subset.copy()
                )  # append the copy of the current state of subset into res
                return

            # to include the current number into the subset
            subset.append(nums[index])
            bfs(index + 1)
            # to not include the current number into the subset
            subset.pop()
            bfs(index + 1)  # this recursive call has an empty subset given to it

        bfs(0)
        return res


s = Solution()
print(s.subsets(nums=[1, 2]))  # [[], [1], [2], [1, 2]]
# print(s.subsets(nums=[3, 4, 0, -1]))
# print(s.subsets(nums=[0]))

# @lc code=end
