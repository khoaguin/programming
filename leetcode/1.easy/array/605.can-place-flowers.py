#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Greedy: Move through the flowerbed and plant the flower on the way
        If we run out of plots, return False. Otherwise return True
        """
        if n == 0:
            return True
        num_plots = len(flowerbed)
        if num_plots == 1:
            return True if flowerbed[0] == 0 else False
        for i in range(num_plots):
            if (
                (i == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0)
                or (
                    0 < i < num_plots - 1
                    and flowerbed[i] == 0
                    and flowerbed[i - 1] == 0
                    and flowerbed[i + 1] == 0
                )
                or (i == num_plots - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0)
            ):
                flowerbed[i] = 1
                n = n - 1

                # Skip the next plot as it can't be used now
                if i < num_plots - 1:
                    i += 1

            # Early exit if all required flowers are planted
            if n <= 0:
                return True

        # print(n)
        # print(flowerbed)
        return n <= 0


s = Solution()
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))  # True
print(s.canPlaceFlowers(flowerbed=[0, 1], n=1))  # False
print(s.canPlaceFlowers(flowerbed=[0], n=1))  # True
print(s.canPlaceFlowers(flowerbed=[0, 1, 0, 1], n=1))  # False
print(s.canPlaceFlowers(flowerbed=[1], n=1))  # False
print(s.canPlaceFlowers(flowerbed=[0, 0, 1, 0, 0], n=1))  # True

# @lc code=end
