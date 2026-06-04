class MinStack:

    def __init__(self):
        self.stack = []
        self.pre = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pre.append(min(val, self.pre[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.pre.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pre[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
