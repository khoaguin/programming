#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        My solution
            Run time: O(n) - we visit each node once. Beats 57.66% of users with Python3
            Space: avg case O(log n). Worst case O(n) when the tree is linear.
                    Beats 8.42% of users with Python3
        """

        def find_max_depth(root: Optional[TreeNode], max_depth: int) -> int:
            if not root:
                # if a node is None, it means that we reached the terminate node.
                # return the max_depth found
                return max_depth
            else:
                # if a node is not None, recursively find the maximum depth of its children nodes
                max_depth = max(
                    find_max_depth(root.left, max_depth + 1),
                    find_max_depth(root.right, max_depth + 1),
                )
                return max_depth

        return find_max_depth(root, 0)

    def maxDepth(self, root: Optional[TreeNode]):
        """
        Simpler code
            Run time beats 93.67% of users with Python3
            Memory beats 22.12% of users with Python3
        """
        if not root:
            return 0
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1


# @lc code=end
