#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#


# @lc code=start

import collections


class MyStack:
    """
    Simplest implementation using a list
        Time Complexity: append and pop operations from both the ends
          using a python List provides O(n) time complexity.

    Result:
        Runtime beats 19.21% of python3 submissions (41 ms)
        Mem usage beats 51.95% of python3 submissions (16.3 MB)
    """

    def __init__(self):
        self._data = []

    def push(self, x: int) -> None:
        # Pushes element x to the top of the stack.
        self._data.append(x)

    def pop(self) -> int:
        # Removes the element on the top of the stack and returns it.
        return self._data.pop()

    def top(self) -> int:
        # Returns the element on the top of the stack.
        return self._data[-1] if len(self._data) > 0 else None

    def empty(self) -> bool:
        # Returns true if the stack is empty, false otherwise.
        return not bool(len(self._data))


class MyStack:
    """
    Implementation using one dequeue (Doubly Ended Queue)
        Time Complexity: append and pop operations from both the ends
          using a python collections.deque() provides O(1) time complexity.

    Note: Must use only standard operations of a queue, which means that only
        push to back (.append), peek/pop from front (index 0), size (len)
        and is empty operations are valid.

    Result:
        Runtime beats 34.01% of python3 submissions (41 ms)
        Mem usage beats 51.95% of python3 submissions (16.3 MB)
    """

    def __init__(self):
        self._data = collections.deque()

    def push(self, x: int) -> None:
        # Pushes element x to the top of the stack.
        self._data.append(x)  # append = push to back
        self._data.rotate(1)

    def pop(self) -> int:
        # Removes the element on the top of the stack and returns it.
        return self._data.popleft()

    def top(self) -> int:
        # Returns the element on the top of the stack.
        return self._data[0] if len(self._data) > 0 else None

    def empty(self) -> bool:
        # Returns true if the stack is empty, false otherwise.
        return not len(self._data)


if __name__ == "__main__":
    #     # Your MyStack object will be instantiated and called as such:
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack._data)
    print(myStack.top())  # return 2
    print(myStack.pop())  # return 2
    print(myStack.empty())  # return False
# @lc code=end
