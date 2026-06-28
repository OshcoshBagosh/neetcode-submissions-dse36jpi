class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Since nums[0] and nums[-1] are neighbors and idea is to apply same
        logic of House Robber
        We can seperate it into 2 sections
        finding the max profit from houses nums[0:n-1]
        finding the max profit from houses nums[1:n]
        then returning the highest profit from both
        """
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        for i in range(len(nums)-1):
            temp = max(nums[i]+ rob1, rob2)
            rob1 = rob2
            rob2 = temp
        res1 = rob2

        rob1, rob2 = 0,0 
        for i in range(1, len(nums)):
            temp = max(nums[i]+ rob1, rob2)
            rob1 = rob2
            rob2 = temp
        res2 = rob2

        return max(res1, res2)
        