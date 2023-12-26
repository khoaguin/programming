#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#


# @lc code=start
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    My solution: Using a modified dfs search to find the path
    """

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root: TreeNode, cur_path: str, paths: List):
            """
            Using modified pre-order DFS traversal.
            Note: No backtracking used, but using a check to solve
                (only add value to current path if a node is not leaf)
            """
            if root is None:
                return
            is_leaf = (not root.left) and (not root.right)
            if not is_leaf:
                cur_path += str(root.val) + "->"
            else:
                cur_path += str(root.val)
                paths.append(cur_path)
            dfs(root.left, cur_path, paths)  # traverse the left subtree
            dfs(root.right, cur_path, paths)  # traverse the right subtree

        paths = []
        dfs(root, "", paths)
        return paths


class Solution:
    """
    Optimized solution with ChaptGPT's help: 
        - Avoid String Concatenation in Recursion: In Python, strings are immutable, so 
            each concatenation creates a new string. This can be inefficient, especially 
            for long paths in deep trees. A more efficient approach is to use a list to 
            keep track of the current path and convert it to a string only when a leaf node is reached.
        - Runtime Complexity: O(n) since we visit each node once
        - Space Complexity: O(N) in the worst case (for a skewed tree) and O(log(N)) for a balanced
            tree, dominated by the depth of the recursive call stack and the length of the path being 
            explored at any given time.
        - Example code run for root = [1, 2, 3, null, 5]
             1
            / \
           2   3
            \
             5
            1. Start at the root (1). current_path = ["1"].
            2. Move to the left child of 1, which is 2. current_path = ["1", "2"].
            3. Since node 2 does not have a left child, we move to its right child, which is 5. 
                current_path = ["1", "2", "5"].
            4. Node 5 is a leaf node, so we add the path to our list of paths: paths = ["1->2->5"].
            5. We then backtrack from node 5 to node 2. After popping, current_path = ["1", "2"].
            6. Backtrack further to the root node 1. After popping, current_path = ["1"].
            7. Move to the right child of 1, which is 3. current_path = ["1", "3"].
            8. Node 3 is a leaf node, so we add the path to our list of paths: 
                paths = ["1->2->5", "1->3"].
            9. Backtrack to the root. After popping, current_path = ["1"].
            10. Since we have explored both children of the root, the DFS is complete.
    """

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root: TreeNode, current_path: List, paths: List) -> None:
            if root is None:
                return

            current_path.append(str(root.val))

            if not root.left and not root.right:  # reaching leaf node
                print("reaching leaf node", root.val)
                paths.append("->".join(current_path))
                print(f"{paths = }")
            else:
                # continue exploring its left and right child
                dfs(root.left, current_path, paths)
                dfs(root.right, current_path, paths)

            # Now we backtrack. Pop the current node from current_path when backtracking
            current_path.pop()

        paths = []
        dfs(root, [], paths)
        return paths


# @lc code=end
