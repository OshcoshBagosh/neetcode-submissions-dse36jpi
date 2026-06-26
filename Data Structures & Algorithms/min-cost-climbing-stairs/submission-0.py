class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = [0] * len(cost)
        stairs[0] = cost[0]
        stairs[1] = cost[1]

        for i in range(2, len(stairs)):
            stairs[i] = cost[i] + min(stairs[i-1], stairs[i-2])
        
        print(stairs)
        return min(stairs[-1], stairs[-2])
