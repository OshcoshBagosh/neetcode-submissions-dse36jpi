class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracks = {"(": ")","[": "]","{": "}"}
        
        for char in s:
            if char in bracks:
                stack.append(bracks[char])
            elif len(stack) > 0 and char == stack[-1]:
                stack.pop()
            else: return False
        
        return len(stack) == 0