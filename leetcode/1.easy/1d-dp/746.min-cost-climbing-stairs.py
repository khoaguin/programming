#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        WRONG SOLUTION:
        We can either start at 0 or 1, and can climb 1 or 2 steps
        Hence, the best next step to take is the minimum cost of the next 1 or 2 step
            The min cost of step i = cost[i] + minimum(cost[i+1], cost[i+2])
            We stop when i = the top = len(cost)
            Then we just need to return the min of start at 0 or start at 1
        """
        total_steps = len(cost)

        if total_steps == 1:
            return cost[0]

        if total_steps == 2:
            return min(cost[0], cost[1])

        def find_min_cost(i: int = 0):
            """
            i is the starting index and can be either 0 or 1
            """
            min_cost = cost[i]

            while i < total_steps - 2:
                print(i)
                next_step = 1 if cost[i + 1] < cost[i + 2] else 2
                min_cost += cost[i + next_step]
                i += next_step
            print(i)
            return min_cost

        return find_min_cost(0)


s = Solution()
s.minCostClimbingStairs([0, 1, 2, 2])


# @lc code=end
