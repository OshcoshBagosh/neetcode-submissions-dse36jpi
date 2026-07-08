class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Brute force: we use recursion to explore all possible combinations of
        coins and return minimum coins used O(c^n)
        Top Down: use a hashmap to store repeated sub problems
        Bottom Up:
        """
        #From out top down approach we know 0 is basecase
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        #i can stand for the amount of coins we are using
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return -1 if dp[amount] == math.inf else dp[amount]


        