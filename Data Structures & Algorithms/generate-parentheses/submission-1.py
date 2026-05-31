class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res =[]
        def dfs(opens, closes):
            if opens == closes == n:
                #add subset to res
                res.append("".join(stack))
                return

            #add open bracket to stack
            if opens < n:
                stack.append("(")
                dfs(opens+1, closes)
                stack.pop()
            #add close bracket to stack
            if closes < opens:
                stack.append(")")
                dfs(opens, closes+1)
                stack.pop()
        dfs(0,0)
        return res
        