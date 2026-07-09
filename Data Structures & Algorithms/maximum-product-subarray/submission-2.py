class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            total = nums[i]
            res = max(res, total)
            for j in range(i+1, len(nums)):
                total = total * nums[j]
                res = max(res, total)

        return res



        