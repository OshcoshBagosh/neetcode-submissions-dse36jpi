class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return highest proft.
        #if negative return 0
        profit = 0
        for i in range(1,len(prices)):
            if(prices[i] - min(prices[0:i]) > profit):
                profit = prices[i] - min(prices[0:i])
                    
        return profit