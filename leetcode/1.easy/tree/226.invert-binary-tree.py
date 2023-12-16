#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursive DFS solution. For each node, it swaps the left and right
        children and then recurses on these children.
        Run time: O(n) - we visit every node once.
        Space complexity: Max size of the recursion stack equals to the depth of the tree
            The worst case is O(n) - the  that the tree is linear
            For a balanced tree, it would be O(log n).
        """
        if root:
            root.right, root.left = self.invertTree(root.left), self.invertTree(
                root.right
            )
            return root


# @lc code=end
