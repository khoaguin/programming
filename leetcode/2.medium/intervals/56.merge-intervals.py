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
        the start of another interval appeared later in the list.
        Loop through the sorted intervals, take an interval and compare its end with
        the start of the next interval; as long as they overlap, we update the end to
        be the max end of the overlapping intervals.
        Time Complexity: sorted has the complexity of  O(n logn)
            The loop has time complexity O(n)
            Hence, the overall time complexity of O(n logn)
        Space Complexity: The sorted_intervals list takes O(n) space
            The res list takes O(n) space
            Hence, the overall space complexity is O(n)
        """
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []

        for i in sorted_intervals:
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)

        return res


s = Solution()
print(s.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge(intervals=[[1, 4], [4, 5]]))
# @lc code=end
