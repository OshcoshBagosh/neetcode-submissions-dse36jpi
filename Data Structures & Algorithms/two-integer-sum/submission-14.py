class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, v in enumerate(nums):
            indexes[v] = i
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in indexes and indexes[diff] != i:
                return [min(i, indexes[diff]), max(i, indexes[diff])]