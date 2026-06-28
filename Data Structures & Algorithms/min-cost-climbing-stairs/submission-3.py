class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1, cost2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost1, cost2)
            cost1 = cost2
            cost2 = cost[i]
        print(cost)
        
        return min(cost[-1], cost[-2])
