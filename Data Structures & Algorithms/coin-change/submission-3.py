class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            m = math.inf
            for c in coins:
                if c <= amount: 
                    m = min(m, 1 + dfs(amount-c))
            memo[amount] = m
            return m
        res = dfs(amount)
        if res == math.inf:
            return -1
        return res
        