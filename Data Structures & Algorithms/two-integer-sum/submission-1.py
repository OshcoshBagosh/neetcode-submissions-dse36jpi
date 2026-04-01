class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {x: i for i, x in enumerate(nums)}

        for i in range(len(nums)):
            difference = target - nums[i]
            if (difference in hashMap and hashMap[difference] != i):
                return [i, hashMap[difference]]


        