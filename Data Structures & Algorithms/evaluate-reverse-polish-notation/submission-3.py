class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arith = ["+", "-", "*", "/"]
        stack = []
        for x in tokens:
            if x == "+":
                stack.append(stack.pop() + stack.pop())
            elif x == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif x == "*":
                stack.append(stack.pop() * stack.pop())
            elif x == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(x))
            
        return stack[len(stack) - 1]

                