class MinStack:
    """
    MinStack should have to stacks, one to keep track of all elements
    the other should keep track of lowest number
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.cur_min = math.inf
        
    def push(self, val: int) -> None:
        self.cur_min = min(self.cur_min, val)
        self.stack.append(val)
        self.min_stack.append(self.cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if not self.min_stack:
            self.cur_min = math.inf
        else:
            self.cur_min = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cur_min
        
