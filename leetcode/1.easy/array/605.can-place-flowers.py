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
        Move through the flowerbed and plant the flower on the way
        If we run out of plots, return False. Otherwise return True
        """
        i = 0
        if len(flowerbed) == 1:
            return not n
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n = n - 1
                    i += 2

        return False if n > 0 else True
        # if i == 0 and :

        # if i == len(flowerbed) - 1:


# s = Solution()
# print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
# print(s.canPlaceFlowers(flowerbed=[0, 1], n=1))
# print(s.canPlaceFlowers(flowerbed=[0], n=1))
# print(s.canPlaceFlowers(flowerbed=[0, 1, 0, 1], n=1))
# print(s.canPlaceFlowers(flowerbed=[1], n=1))

# @lc code=end
