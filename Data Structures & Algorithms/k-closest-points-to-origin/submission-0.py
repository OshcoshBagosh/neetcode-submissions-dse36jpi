class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        min_heap = []

        for p in points:
            x, y = p
            distance = math.sqrt((0-x)**2 + (0-y)**2)
            heapq.heappush(min_heap, (distance, p))
        
        
        res = []

        while len(res) != k and min_heap:
            point = heapq.heappop(min_heap)[1]
            res.append(point)
        
        return res
        