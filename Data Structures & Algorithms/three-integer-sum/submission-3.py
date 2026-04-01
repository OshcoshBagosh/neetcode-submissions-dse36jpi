class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort the array
        result = []
        We will go through each index in the array nums.
        we will have a left and right pointer 
        left = i + 1 and right = len(num) - 1
        if nums[i] is greater than 0 end loop
        while (left > right)
        if total > 0:
            right -= 1
        elif total < 0:
            left += 1
        else:
            result.append[nums[left], nums[right], nums[i]]
            left += 1
            right -= 1
        
        return result
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
        








