#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 step: we have 1 way to climb the first step
        2 steps: we have 2 ways to climb
        nth steps: we can reach the nth step from either the (n-1)th step or the (n-2)th step
        For example, when n = 3:
            - Reach from the 2nd step: we have 2 ways (1+1+1 or 2+1)
            - Reach from the 1st step: we have only one way (1+2)
            => 3 ways
        => This is the fibonnaci sequence. Note that naive Fibonnaci will not be
        able to reach the time limit
        Time Complexity: O(n) - we loop through the range of n steps
        Space Complexity: O(n) - used to store the array
        """
        res = [1, 2]

        def fibonnaci(n: int) -> None:
            for i in range(2, n):
                res.append(res[i - 1] + res[i - 2])

        fibonnaci(n)
        return res[n - 1]

    def climbStairs(self, n: int) -> int:
        """
        Further improve space complexity to O(1)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev_step, current_step = 1, 2
        for _ in range(3, n + 1):
            next_step = prev_step + current_step
            prev_step = current_step
            current_step = next_step
        return next_step


s = Solution()
print(s.climbStairs(5))

# @lc code=end
