#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#


# @lc code=start
class MyStack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        # Pushes element x to the top of the stack.
        self.data.append(x)

    def pop(self) -> int:
        # Removes the element on the top of the stack and returns it.
        return self.data.pop()

    def top(self) -> int:
        # Returns the element on the top of the stack.
        return self.data[-1] if len(self.data) > 0 else None

    def empty(self) -> bool:
        # Returns true if the stack is empty, false otherwise.
        return not bool(len(self.data))


if __name__ == "__main__":
    #     # Your MyStack object will be instantiated and called as such:
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.data)
    print(myStack.top())  # return 2
    print(myStack.pop())  # return 2
    print(myStack.empty())  # return False
# @lc code=end
