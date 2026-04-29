class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            max_num = nums[i]
            for j in range(i, i + k):
                max_num = max(max_num, nums[j])
            result.append(max_num)

        return result
        