#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Recursive Solution
        Time Complexity: O(n+m) where n & m are the lengths of the lists
            Beats 9.84% Python3 solutions
        Time Complexity: O(n+m)
            Beats 28.72% Python3 solutions
        """
        # base case
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        # recursive case
        if head1.val <= head2.val:
            head1.next = self.mergeTwoLists(head1.next, head2)
            return head1
        else:
            head2.next = self.mergeTwoLists(head1, head2.next)
            return head2


# @lc code=end
