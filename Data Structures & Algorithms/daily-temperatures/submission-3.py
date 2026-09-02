class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        We can use a monotonic stack
        [30,38,30,36,35,40,28]
        stack = [40, ]
        res = [-1,-1,-1,-1,1,-1,-1]
        """
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)-1, -1, -1):
            if stack:
                while stack and temperatures[i] >= stack[-1][0]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1][1] - i

            stack.append((temperatures[i], i))

        return res
        