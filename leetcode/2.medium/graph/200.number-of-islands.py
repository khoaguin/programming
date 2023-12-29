#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque
from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Using BFS to traverse through all the grid node
        We need to check if a node is already explored and
            if it belongs to an existing island / a new island / water
        Using collections.deque to keep track of the nodes to visit
            since deque.append() and .popleft() are O(1)
        maximum neighboring lands of a (i,j) land is 4 lands
            (since only horizontally and vertically):
            (i, j+1), (i, j-1), (i+1, j), (i-1, j)
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        def bfs() -> None:
            visited = set()
            to_visit = deque()
            i, j = 0, 0
            to_visit.append(grid[i][j])
            while len(to_visit) > 0:
                current_node = to_visit.popleft()
                print(current_node)
                visited.add(current_node)
                for neighboring_idx in neighboring_indices(i, j):
                    neighbor = grid[neighboring_idx[0]][neighboring_idx[1]]
                    print(f"{neighbor = }")
                    if neighbor not in visited:
                        to_visit.append(neighbor)

        def neighboring_indices(i, j) -> List[Tuple]:
            print(f"finding neighboring_indices{(i, j)}")
            all_neighboring_indices = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            return [idx for idx in all_neighboring_indices if is_valid(idx[0], idx[1])]

        def is_valid(i, j) -> bool:
            return i >= 0 and j >= 0 and i < len(grid[0]) and j < len(grid[1])

        print(bfs())
        return 1


s = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
s.numIslands(grid)

# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"],
# ]
# s.numIslands(grid)

# @lc code=end
