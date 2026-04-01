class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set(nums)
        ht = {}
        for num in set1:
            ht.update({num: False})
        
        for num in nums:
            if (ht[num] == False):
                ht[num] = True
            else:
                return True
        return False
        