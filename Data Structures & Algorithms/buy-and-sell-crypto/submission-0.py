class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return highest proft.
        #if negative return 0
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if(prices[j] - prices[i] > profit):
                    profit = prices[j] - prices[i]
                    
        return profit