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
        from typing import Optional

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Naive Approach
        First we need a function to check if 2 trees are the same. Then,
        - If the root's and subRoot's trees are same, return True
        - If not, recursively find out if the root's left subtree OR the root's right 
            subtree is equal to the subRoot's tree

        Runtime Complexity: O(m * n) where m and n are the number of nodes in the root 
                and subRoot's trees (Beats 93% of users with Python3)
        Space Complexity: average case O(max(height1, height2)). Worst case: O(max(m, n)). 
                Beats 6.47% of users with Python3
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


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Merkle hashing
        For each node in both trees, find its merkle hash value that 
        represents the hash of its left child, value and right child.
        Then find out if all the merkles in the subRoot tree also present in the root tree
        - Runtime Complexity: O(n + m) where n = number of nodes in root, and m is the 
            number of nodes in subRoot. The function compute_merkle traverses each node  
            of both the root and subRoot trees once to compute their Merkle hashes.
            Beats 94.50% of users with Python3
        - Space Complexity: O(n + m). The space complexity is driven by the storage of 
            Merkle hashes for each node in both trees and the call stack for recursive 
            calls. The hash sets tree_hash_set and subtree_hash_set store a unique hash 
            for each node in root and subRoot, respectively. The depth of the recursive 
            calls contributes additional space complexity, but this is generally smaller 
            than the space needed for storing the hashes.
            Beats 6.53% of users with Python3
        """
        from hashlib import sha256
        from typing import Set

        def hashify(node):
            node = node.encode('utf-8')
            S = sha256()
            S.update(node)
            return S.hexdigest()
        
        def compute_merkle(node: TreeNode, hash_set: Set) -> None:
            """
            Recursively goes through the tree to find the merkle hash values for each node
                Runtime: O(n)
            """
            if not node:
                return "#"
            h = hashify(
                (compute_merkle(node.left, hash_set)
                + str(node.val)
                + compute_merkle(node.right, hash_set)
                )
            )
            hash_set.add(h)
            return h
        
        tree_hash_set = set()
        compute_merkle(root, tree_hash_set)
        subtree_hash_set = set()
        compute_merkle(subRoot, subtree_hash_set)
        
        is_subtree = True
        for h in subtree_hash_set:
            if h not in tree_hash_set:
                is_subtree = False
        return is_subtree


# @lc code=end
