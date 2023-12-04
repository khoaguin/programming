#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        My Solution
        Time Complexity: O(l*n) where l is the length of the first string, n is the number of all strings
            (beats 17.34% Python3 solutions)
        Memory Complexity: O(l)
            (beats 13.52% Python3 solutions)
        """
        i = 0
        first_str = strs[0]
        common_prefix = ""
        while i < len(first_str):
            is_a_common_prefix = True
            for s in strs[1:]:
                try:
                    if s[i] != first_str[i]:
                        is_a_common_prefix = False
                except IndexError:
                    return common_prefix

            if is_a_common_prefix:
                common_prefix += first_str[i]
            else:
                return common_prefix

            i += 1

        return common_prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Better Solution: Using the trick of sorting the list lexicographically and
            comparing only the first and last strings to find the common prefix

        Time Complexity: sorted has O(n log n). So the algo has O(nlog(n) + l)
            where n is the number of strings and l is the min of the length of the first and last string
            (beats 97% Python3 solutions)
        Memory Complexity: O(n)
            (beats 13.52% Python3 solutions)
        """
        sorted_strs = sorted(strs)  # sort lexicographically
        first = sorted_strs[0]
        last = sorted_strs[-1]
        common_prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix += first[i]
            else:
                return common_prefix

        return common_prefix


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["cir", "car"]) == "c"
    assert s.longestCommonPrefix(["abab", "aba", "abc"]) == "ab"
# @lc code=end
