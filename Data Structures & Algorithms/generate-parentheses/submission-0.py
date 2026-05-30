class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res =[]
        def dfs(opens, closes):
            if opens == closes == n:
                res.append("".join(stack))
                return

            if opens < n:
                stack.append("(")
                dfs(opens+1, closes)
                stack.pop()

            if closes < opens:
                stack.append(")")
                dfs(opens, closes+1)
                stack.pop()
        dfs(0,0)
        return res
        