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
        - Repeated calls of bfs() on water nodes
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

        def inside_grid(idx: Tuple[int], grid: List[List[str]]) -> bool:
            (i, j) = idx
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

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


class Solution:
    """
    DFS Solution: Iterate through all the nodes on the grid. If the node is land,
        use DFS to explore connected lands. Remember to mark the visited lands
    Time Complexity: O(h*w) where h and w are the height and width of the grid
        The reason is that in the worst case, for each node, we may use DFS to visit all
        other nodes, e.g. imagine all nodes are land
    Space Complexity: O(h*w) since the space complexity mainly comes from the recursion
        stack used in DFS. In the worst case (e.g., the grid is entirely land), the
        depth of the stack can be as large as the number of cells in the grid.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            grid[i][j] = "#"  # important: mark the land as explored
            # print(grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # print(f"Finding land at ({i}, {j}). Exploring neighboring nodes")
                    dfs(i, j, grid)
                    num_islands += 1
        return num_islands


class Solution:
    """
    Optimized BFS solution: Make sure that each node is only visited once and
        only run BFS when we find out a land node is the start node of an unvisited island
        1. Iterate over the grid: Go through each cell in the grid.
        2. Check for Unvisited Land: When you find a land cell ("1") that hasn't been
            visited, it indicates the start of a new island.
        3. Perform BFS: Use BFS to explore the entire island starting from this cell.
        4. Mark Visited Cells: During BFS, mark each visited cell to avoid revisiting it.
        5. Count Islands: Each BFS initiation counts as discovering a new island.
    Time Complexity: O(M*N), where M is the number of rows and N is the number of
        columns in the grid. Each cell is visited at most once.
    Space Complexity: O(min(M, N)) in the worst case. The maximum size of the queue
        (used in BFS) can be the maximum of the width or height of the grid, which
        happens in a worst-case scenario when the grid is filled with lands.
    """

    from collections import deque
    from typing import Set, Tuple

    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j, grid, visited) -> None:
            to_visit = deque()
            to_visit.append((i, j))
            while to_visit:
                i, j = to_visit.popleft()
                # visit neighboring land nodes
                neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for n in neighbors:
                    ni = i + n[0]
                    nj = j + n[1]
                    if (
                        0 <= ni < len(grid)
                        and 0 <= nj < len(grid[0])
                        and grid[ni][nj] == "1"
                        and (ni, nj) not in visited
                    ):
                        to_visit.append((ni, nj))
                        visited.add((ni, nj))

        num_islands = 0
        visited: Set[Tuple] = set()
        width, height = len(grid), len(grid[0])
        for i in range(width):
            for j in range(height):
                if grid[i][j] == "1" and (i, j) not in visited:
                    print(f"Find new land that is a start of an island at ({i}, {j})")
                    bfs(i, j, grid, visited)
                    num_islands += 1
        return num_islands


s = Solution()
# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"],
# ]
# print(s.numIslands(grid))

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(grid)
print(s.numIslands(grid))

# @lc code=end
