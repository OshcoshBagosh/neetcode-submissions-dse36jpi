class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        res = upper
        while lower <= upper:
            k = (upper + lower) // 2
            totaltime = 0
            for pile in piles:
                totaltime += math.ceil(float(pile)/k)
            if totaltime <= h:
                res = k
                upper = k - 1
            else:
                lower = k + 1
        
        return res