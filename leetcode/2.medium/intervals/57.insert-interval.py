#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Overlapping = when the end of an interval is bigger or equal than
        the start of another interval appeared later in the list
        Bruteforce: For each interval, check all later intervals in the list
        """
        i = 0
        while i < len(intervals):
            print(f"checking {intervals[i]}")
            for j in range(i + 1, len(intervals)):
                print(f"checking {intervals[j]}")
                if intervals[i][1] >= intervals[j][0]:
                    print(f"detecting overlap - merge")

            i += 1
            print()


s = Solution()
s.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])

# @lc code=end
