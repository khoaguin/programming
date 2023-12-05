#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        """
        Iterative solution
        Run time: O(n) - beats 58% Python3 solutions
        Memory: O(1) - beats 54% Python3 solutions
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


# Have to run or submit to the server to test


# @lc code=end
