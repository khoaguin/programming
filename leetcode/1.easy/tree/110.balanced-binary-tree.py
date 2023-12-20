#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    is_balanced: bool = True

    def depth(self, root: Optional[TreeNode]):
        """
        Find the maximum depth of the tree and check
        if the tree is balanced when finding depth of each node
        """
        if not root:
            return 0
        else:
            left_depth = self.depth(root.left)
            right_depth = self.depth(root.right)
            # check if the tree is balanced
            if abs(left_depth - right_depth) > 1:
                self.is_balanced = False
            return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """A binary tree in which the depth of the two subtrees of every node never differs by more than one
        Run time: Visit ech node once to compute depth => O(n). Each balanced check take O(1)
                  => Overall O(n)
        Space: The recursion stack takes O(n) for a linear tree (worst case). Average case is O(h) where h is the tree's height
        """
        self.depth(root)
        return self.is_balanced


# @lc code=end
