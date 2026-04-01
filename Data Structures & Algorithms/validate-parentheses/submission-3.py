class Solution:
    def isValid(self, s: str) -> bool:
        """
        
        """
        if len(s) % 2 != 0:
            return False

        openBrack = ("(", "[", "{")
        closeBrack = (")", "]", "}")

        stack = []

        for char in s:
            if char in openBrack:
                stack.append(char)
                continue
            elif char in closeBrack:
                if len(stack) == 0:
                    return False
                if char == ")" and stack.pop() != "(":
                    return False
                elif char == "]" and stack.pop() != "[":
                    return False
                elif char == "}" and stack.pop() != "{":
                    return False
        
        return len(stack) == 0
        