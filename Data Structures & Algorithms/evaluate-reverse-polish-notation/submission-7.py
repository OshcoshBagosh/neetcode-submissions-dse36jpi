class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    x, y = stack.pop(), stack.pop()
                    stack.append(y - x)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token == "/":
                    x, y = stack.pop(), stack.pop()
                    stack.append(int(float(y / x)))

        return stack[0]