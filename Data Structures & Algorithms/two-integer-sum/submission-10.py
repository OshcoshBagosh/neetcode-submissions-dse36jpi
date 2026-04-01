class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for x in range(len(nums)):
            ht[nums[x]] = []
        for x in range(len(nums)):
            ht[nums[x]].append(x)
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in ht:
                if(nums[x] == diff and len(ht[diff]) > 1):
                    return [ht[diff][0], ht[diff][1]]
                if (x != ht[diff][0]):
                    if(x > ht[diff][0]):
                        return [ht[diff][0], x]
                    else:
                        return [x, ht[diff][0]]

                
        


        