class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """wordDict = set(wordDict)
        memo = {}
        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return True
            
            for end in range(start+1, len(s)+1):
                prefix = s[start:end]

                if prefix in wordDict and dfs(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False"""

        dp = [False] * (len(s) + 1)
        #basecase
        dp[len(s)] = True
        wordDict = set(wordDict)

        for start in range(len(s)-1, -1, -1):
            for end in range(start+1, len(s)+1):
                prefix = s[start: end]
                if dp[end] and prefix in wordDict:
                    dp[start] = True
    
        return dp[0]

        