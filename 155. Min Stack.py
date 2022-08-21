class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.min_sub = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.min = val
            self.min_sub.append(val)
        elif self.min >= val:
            self.min_sub.append(self.min - val)
            self.min = val
        self.stack.append(val)
        
                
    def pop(self) -> None:
        if self.stack != []:
            if self.stack.pop() == self.min:
                self.min += self.min_sub.pop()

    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack != []:
            return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()