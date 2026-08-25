class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        for s in range(len(stones)):
            stones[s] *= - 1

        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            stone_x = heapq.heappop(stones)
            if stone_x == stones[0]:
                heapq.heappop(stones)
            else:
                stone_y =stone_x - stones[0]
                heapq.heappop(stones)
                heapq.heappush(stones, stone_y)
                
                

        print(stones)
        if stones:
            return stones[0] * -1
        else:
            return 0



        