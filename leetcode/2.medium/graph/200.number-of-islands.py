#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque
from typing import List, Set, Tuple


class Solution:
    """
    First solution: Works but is too slow. Reasons:
        -
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Using BFS to traverse through the grid
        We need to check if a node is already explored and
            if it belongs to an existing island / a new island / water
        Using collections.deque to keep track of the nodes to visit
            since deque's append() and popleft() methods are O(1)
        maximum neighboring lands of a (i,j) land is 4 lands
            (since only horizontally and vertically):
            (i, j+1), (i, j-1), (i+1, j), (i-1, j)
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        def bfs(starting_idx: Tuple[int]) -> Tuple[Set[Tuple[int]], bool]:
            visited = set()  # keep the set of visited indices in the grid
            to_visit = deque()  # keep the queue of nodes' indices to visit in the grid
            to_visit.append(starting_idx)
            first_node = grid[starting_idx[0]][starting_idx[1]]
            on_land = True if first_node == "1" else False
            while len(to_visit) > 0:
                # visit a node
                current_node_idx = to_visit.popleft()
                current_node_value = grid[current_node_idx[0]][current_node_idx[1]]
                # print(f"visiting node {current_node_value} at idx {current_node_idx}")
                visited.add(current_node_idx)
                # visit the neigboring nodes (if they are not yet visited)
                for neighboring_idx in neighbors(current_node_idx, grid, on_land):
                    # print(f"{neighboring_idx = }")
                    if neighboring_idx not in visited:
                        to_visit.append(neighboring_idx)
            return visited, on_land

        def neighbors(
            idx: Tuple[int], grid: List[List[str]], on_land: bool
        ) -> List[Tuple]:
            """
            Given the index tuple of a node on the grid, return its neighboring indices
            """
            (i, j) = idx
            neighboring_indices = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
            inside_grid_neighbors = [
                idx for idx in neighboring_indices if inside_grid(idx, grid)
            ]
            valid_neighbors = []
            for idx in inside_grid_neighbors:
                ni, nj = idx
                if on_land:
                    if grid[ni][nj] == "1":
                        valid_neighbors.append(idx)
                else:
                    if grid[ni][nj] == "0":
                        valid_neighbors.append(idx)
            return valid_neighbors

        def inside_grid(idx: Tuple[int], grid: List[List[str]]) -> bool:
            (i, j) = idx
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

        # get the set of all indices in the grid
        to_visit = set(
            [(i, j) for i, row in enumerate(grid) for j, _ in enumerate(row)]
        )
        num_islands = 0
        while len(to_visit) > 0:
            start_indx = to_visit.pop()
            visited, on_land = bfs(
                starting_idx=start_indx
            )  # start at the origin. Can be any index

            print(f"{start_indx = }, {visited = }, {on_land = }")
            if on_land:
                num_islands += 1
            to_visit -= visited
            print(f"{to_visit = }")

        return num_islands


s = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(s.numIslands(grid))

# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"],
# ]
# print(s.numIslands(grid))

# @lc code=end
