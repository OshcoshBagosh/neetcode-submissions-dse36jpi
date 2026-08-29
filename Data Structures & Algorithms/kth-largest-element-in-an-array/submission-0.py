class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        i = k
        while nums and k > 1:
            heapq.heappop(nums)
            k -= 1

        return heapq.heappop(nums) *-1