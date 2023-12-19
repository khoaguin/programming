#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Diameter of a tree = Max value of depth(leftSubtree) + depth(rightSubtree) (at any node of the tree).
        Runtime
            - for each node, find_max_depth() recursively traverses the entire treeto find the maximum depth,
                so it's O(n))
            - for each node, find_diameter() calls find_max_depth twice, so it's O(2n) for each node.
            - Hence, the overall time complexity is O(n) * O(2n) = O(n^2).
            Runtime beats 5.08% of users with Python3
        Space:
            The maximum depth of the recursion stack is equal to the height of the binary tree.
            In the worst case, when the binary tree is completely unbalanced (essentially a linked list),
                the height of the tree can be O(n).
            Therefore, the space complexity of this algorithm is O(n) in the worst case.
            Memory beats 5.63% of users with Python3
        """

        def find_max_depth(node: Optional[TreeNode], max_depth: int) -> int:
            """
            Helper function: Find max depth of a node
            """
            if not node:
                return max_depth
            else:
                return max(
                    find_max_depth(node.left, max_depth + 1),
                    find_max_depth(node.right, max_depth + 1),
                )

        def find_diameter(root: Optional[TreeNode], diameter) -> int:
            if not root:
                return 0  # diameter of a termination node is 0
            else:
                root_diameter = (
                    find_max_depth(root.left, 1) + find_max_depth(root.right, 1) - 2
                )
                return max(
                    root_diameter,
                    find_diameter(root.left, root_diameter),
                    find_diameter(root.right, root_diameter),
                )

        return find_diameter(root, 0)


class Solution:
    """
    Similar idea like above, but with better implementation
    Essentially, we find the diameter inside the find_depth function,
    so we don't repeat the process
    Run time complexity:
        - For each node, we call self.find_depth twice on a left and right children.
            Each call visits each node in the tree onces, hence the complexity is O(2n)
        - Hence, the overall time complexity is O(n)
        - Beats 93.41% of users with Python3
    Space complexity:
        - The maximum depth of the recursion stack is equal to the height of the binary tree
            => worst case = O(n)
        - Beats 42.45% of users with Python3
    """

    diameter = 0

    def find_depth(self, node: Optional[TreeNode]) -> int:
        """
        Find the diameter of a node in the tree through its children depth.
        Save the max diameter in self.diameter
        """
        if node:
            left_depth = self.find_depth(node.left) if node.left else 0
            right_depth = self.find_depth(node.right) if node.right else 0
            diameter = left_depth + right_depth
            if diameter > self.diameter:
                self.diameter = diameter
            return max(right_depth, left_depth) + 1  # depth of the current node
        else:
            return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_depth(root)
        return self.diameter


# @lc code=end
