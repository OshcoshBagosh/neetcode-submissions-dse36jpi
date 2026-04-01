class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #returns an int count of consecutive nums
        #to be consecutive, each num is > than the previous by 1
        """
        To save time we can convert nums into a set to remove any
        duplicates which runs at O(n)
        """

        numsSet = set(nums)
        sequences = {}

        for num in numsSet:
            if num - 1 not in nums:
                sequences[num] = [num]

        for key in sequences:
            i = 1
            while(key + i in numsSet):
                sequences[key].append(key + i)
                i += 1
        
        result = 0
        for key in sequences:
            if len(sequences[key]) > result:
                result = len(sequences[key])

        return result
 
            