class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        one, two = 1, 1
        for i in range(1, n):
            res = one + two
            one, two = two, one + two
        
        return res