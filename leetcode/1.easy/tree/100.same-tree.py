#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        If roots are not None and same, recursively check if the left nodes and right nodes of the trees are same.
        If we reach the termination nodes of both trees, return True
        Run time: Worst case is O(n) since we visit each node once
                  Best case is when we find a mismatch and return early
                  Beats 50.12% of users with Python3
        Space: O(tree height) average case, O(n) worst case when the trees are skewed
               Beats 75.54% of users with Python3
        """

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False


# @lc code=end
