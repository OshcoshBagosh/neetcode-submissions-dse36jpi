class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort the array
        We will go through each index in the array.
        we will have a left and right pointer 
        if the index is between 0 and len(num) - 1 
        left = 0 and right = len(num) - 1
        if not then left can be 1 or right can be len(num) - 2
        result = []
        switch = 0
        while (left > right)
            sum = nums[left] + nums[right] + nums[index]
            if sum == 0
                result.append([nums[left], nums[right], nums[i]])
            elif switch == 0
                left ++
                switch == 1
            elif switch = 1
                right --
                switch = 0
        return []
        """
        #[-1,0,1,2,-1,-4]
        #[-4, -1, -1, 0, 1, 2]
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums)-1

            while(left < right):
                total = nums[left] + nums[right] + nums[i]        
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
        








