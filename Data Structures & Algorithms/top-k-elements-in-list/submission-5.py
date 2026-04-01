class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We could use the Counter data structure to get the frequency
        of each number

        Then we could use max heap to return the highest frequency
        numbers k times.
        """

        import collections
        import heapq

        freq = Counter(nums)
        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


        