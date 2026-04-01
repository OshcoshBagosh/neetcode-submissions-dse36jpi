class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            if nums[i] not in indexes:
                indexes[nums[i]] = [i]
            else:
                indexes[nums[i]].append(i)

        for num in nums:
            val = target - num
            print(val)
            
            if(val in indexes):
                if val == num and len(indexes[num]) > 1:
                    return indexes[num]
                elif val == num and len(indexes[num]) <= 1:
                    continue
                return [indexes[num][0], indexes[val][0]]
