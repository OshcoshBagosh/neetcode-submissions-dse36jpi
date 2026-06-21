class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        price = math.inf

        for i in range(len(prices)):
            for j in range(len(prices)):
                if i == j:
                    continue
                total = prices[i] + prices[j]
                price = min(price, total)

        if price > money:
            return money

        return money - price
        