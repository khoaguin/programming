#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
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
        merged_indices = []
        merged_intervals = []
        i = 0
        while i < len(intervals):
            for j in range(i + 1, len(intervals)):
                if intervals[i][1] >= intervals[j][0]:
                    print(f"Detecting overlap. Merge {intervals[i]} and {intervals[j]}")
                    merged = [intervals[i][0], intervals[j][1]]
                    merged_indices.append((i, j))
                    merged_intervals.append(merged)
            i += 1

        for i in merged_indices:
            # print(i)
            intervals[i[0]] = merged_intervals[i[0]]
            del intervals[i[1]]

        return intervals


s = Solution()
# s.merge([[1, 4], [4, 5]])
print(s.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge(intervals=[[1, 4], [4, 5]]))
# @lc code=end
