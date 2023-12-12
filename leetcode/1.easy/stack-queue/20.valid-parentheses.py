#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Runtime beats 52.36 % of python3 submissions
        Mem usage beats 5.54 % of python3 submissions (16.5 MB)
        """
        if len(s) <= 1:
            return False

        stack = deque()
        is_valid = True
        i = 0
        paren_map = {")": "(", "}": "{", "]": "["}
        while i < len(s) and is_valid:
            try:
                c = s[i]
                if c in paren_map:
                    is_valid = stack.pop() == paren_map[c]
                else:
                    stack.append(c)
            except Exception:
                is_valid = False
            i += 1

        return is_valid and len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("(("))
# @lc code=end
