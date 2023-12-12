#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from typing import List


class MyQueue:
    """
    Use a List as a stack
    Note: Must use only standard operations of a stack:
    push to top (append), peek/pop from top (index -1), size (len)
        Run time: Beats 98.84% of users with Python3
        Memory: Beats 83.00% of users with Python3
    """

    _queue: List

    def __init__(self):
        self._queue = []

    def push(self, x: int) -> None:
        self._queue.append(x)
        self._queue = self._queue[-1:] + self._queue[:-1]

    def pop(self) -> int:
        return self._queue.pop()

    def peek(self) -> int:
        return self._queue[-1]

    def empty(self) -> bool:
        return not len(self._queue)


if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj._queue)  # [3, 2, 1]
    print(obj.peek())  # 1
    print(obj.pop())  # 1
    print(obj._queue)  # [3, 2]
    print(obj.empty())  # False

# @lc code=end
