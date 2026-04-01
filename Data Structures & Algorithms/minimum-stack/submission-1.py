import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_num = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_num = min(val, self.min_num)
        self.min_stack.append(self.min_num)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if len(self.min_stack) == 0:
            self.min_num = math.inf
        else:
            self.min_num = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
