class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        h = [0] * len(nums)
        h[0] = nums[0]
        h[1] = nums[1]
        for i in range(2, len(nums)):
            h[i] = nums[i] + max(h[i-2], h[i-3])

        return max(h[-1], h[-2])
        