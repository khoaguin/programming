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


class Solution:
    """
    Since we can only climb 1 or 2 stairs at a time, the min cost to reach the
    top step (nth) step, or min_cost(n), is the minimum of min_cost(n-1) and min_cost(n-2)
    This pattern reveals a pattern for dynamic programming
    Note that except for the last step, we have to add the cost of the current step i into
    min(min_cost(i-1), min_cost(i-2))
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Naive recursive solution (Recursive Top Down)

        Time Complexity: The time complexity of this algorithm is driven by the
            number of recursive calls made. Here, each call to min_cost spawns two
            more calls (for n - 1 and n - 2). This forms a binary tree of recursive
            calls, with the depth of the tree being approximately n.
                At the first level, there's 1 call.
                At the second level, there are 2 calls.
                At the third level, there are 4 calls.
                ...
                At the nth, there are 2^(n-1) calls
            This is a characteristic of exponential growth,
            so the time complexity is O(2^n)
        Space Complexity: The space complexity is determined by the maximum depth of
            the recursion stack. In the worst case, the stack will have a depth equal
            to the length of the input, n. Thus, the space complexity is O(n), which
            accounts for the recursive call stack.
        """

        def min_cost(cost: List[int], n: int):
            # handle some base cases
            if n == 0 or n == 1:
                return cost[n]
            return cost[n] + min(min_cost(cost, n - 1), min_cost(cost, n - 2))

        n = len(cost)
        return min(min_cost(cost, n - 1), min_cost(cost, n - 2))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Optimization1: Recursion with memoization (Top Down DP)

        Time Complexity: With memoization, each unique call to find_min_cost is
            made only once. The results for each step n are stored in the list min_costs,
            and subsequent calls for the same n simply return the stored value
            instead of recomputing it. Since there are n steps, and each step is
            calculated only once, the total number of calculations is n. Therefore, the time complexity is reduced to
        Space Complexity:
            Memoization Array: The space complexity is primarily determined by the size
                of the min_costs array, which is directly proportional to the number of steps n.
            Recursive Call Stack: Additionally, the recursive call stack will also
                contribute to the space complexity. In the worst case, the maximum depth
                of the recursive call stack will be n (when recursively calling down to the base case).
            Combining these two factors, the space complexity remains O(n), where n is
                the length of the cost list
        """
        min_costs: List[int] = [0] * len(cost)

        def find_min_cost(cost: List[int], n: int) -> int:
            # handle some base cases
            if n == 0 or n == 1:
                return cost[n]
            if min_costs[n] != 0:
                return min_costs[n]
            min_costs[n] = cost[n] + min(
                find_min_cost(cost, n - 1), find_min_cost(cost, n - 2)
            )
            # print(f"{n = }, {min_costs[n] = }")
            return min_costs[n]

        n = len(cost)
        return min(find_min_cost(cost, n - 1), find_min_cost(cost, n - 2))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Optimization2: Iterative solution using the tabular method
        Time Complexity: O(n) since we iterate through the `cost` list once
        Space Complexity: O(n) since we keep the min_costs list with
            the same size as the input cost list
        """
        n = len(cost)
        min_costs: List[int] = []

        i = 0
        while i < len(cost):
            if i < 2:
                min_costs.append(cost[i])
            else:
                min_costs.append(cost[i] + min(min_costs[i - 1], min_costs[i - 2]))
            i += 1

        print(min_costs)

        return min(min_costs[n - 1], min_costs[n - 2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Optimization3: Iterative solution with O(1) space complexity
        Time Complexity: O(n) since we iterate through the list `cost` once
        Space Complexity: O(1) since we only keep a constant amount of variables
            when the length of `cost` increases
        """
        current_min_cost = 0
        prev2 = cost[0]  # cost of the i-2 step
        prev1 = cost[1]  # cost of the i-1 step
        i = 2
        while i < len(cost):
            current_min_cost = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current_min_cost
            i += 1

        return min(prev1, prev2)


s = Solution()
print(s.minCostClimbingStairs([0, 1, 2, 2]))


# @lc code=end
