#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Solution based on merge intervals:
            Insert the newInterval into intervals
            Sort the new intervals based on start_i
            Merge the sorted intervals
            Time Complexity: O(n logn)
            Space Complexity: O(n)
        This solution works, but is inefficient since it sort the `intervals` list again
        given that the provided list was already sorted
        """
        intervals.append(newInterval)
        sorted_intervals = sorted(intervals, key=lambda x: x[0])  # O(n logn)
        # print(sorted_intervals)
        res = []
        for i in sorted_intervals:
            if res and i[0] <= res[-1][1]:
                # merging
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        print(res)
        return res


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Optimized solution: Loop through the intervals (already sorted) and insert on the fly
            Time Complexity: O(n) where n is the number of intervals in `intervals`
                because `list.append` function takes O(1) time
            Space Complexity: O(n) since the space needed is proportional to the number of intervals
        """
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < s:  # non-overlapping intervals that are smaller than newInterval
                left.append(i)
            elif i[0] > e:  # non-overlapping intervals that are bigger than newInterval
                right.append(i)
            else:  # merging intervals
                s = min(s, i[0])
                e = max(e, i[1])
        res = left + [[s, e]] + right

        return res


s = Solution()
# s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
# @lc code=end
