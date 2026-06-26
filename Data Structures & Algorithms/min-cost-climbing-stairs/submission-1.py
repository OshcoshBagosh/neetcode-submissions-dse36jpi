class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        We can use a bottom up approach to calculate to calculate the min
        cost of steps
        """
        #The base case is the smallest possible sub problem
        stairs = [0] * len(cost)
        #since we can only take 2 steps, both index 0 and 1 will be basecase
        stairs[0] = cost[0]
        stairs[1] = cost[1]

        for i in range(2, len(stairs)):
            #calcuate step by adding min cost from previous steps to curr
            stairs[i] = cost[i] + min(stairs[i-1], stairs[i-2])
            
        #return min of last 2 steps
        return min(stairs[-1], stairs[-2])
