class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        left = 0
        
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit > largest:
                largest = profit
            if prices[left] > prices[right]:
                left = right

        return largest
        