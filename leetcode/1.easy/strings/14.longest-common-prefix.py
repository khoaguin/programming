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
        Time Complexity: O() - beats 17.34% Python3 solutions
        Memory Complexity: O() - beats 13.52% Python3 solutions
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


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["cir", "car"]))

# @lc code=end
