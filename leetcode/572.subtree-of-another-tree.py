#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Naive Approach
        First we need a function to check if 2 trees are the same. Then,
        - If the root's and subRoot's trees are same, return True
        - If not, recursively find out if the root's left subtree OR the root's right subtree is equal to the subRoot's tree

        Runtime Complexity: O(m * n) where m and n are the number of nodes in the root and subRoot's trees (Beats 45.66% of users with Python3)
        Space Complexity: average case O(max(height1, height2)). Worst case: O(max(m, n)). Beats 6.47% of users with Python3
        """

        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            """
            Helper function to find if 2 trees are the same given their root nodes
            """
            # if both roots are None
            if p is None and q is None:
                return True
            # if only one is None, or if their values are different
            if p is None or q is None or p.val != q.val:
                return False
            # the remaining case is that 2 roots are not None and their values are the same
            # then we recursively find if the left subtrees and right subtrees are the same
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        if root is None:
            return False
        if is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# @lc code=end
