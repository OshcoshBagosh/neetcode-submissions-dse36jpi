class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ls = [False] * len(nums)
        print(ls)
        def dfs(subset, arr):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                if arr[i]:
                    continue

                subset.append(nums[i])
                arr[i] = True

                dfs(subset, arr)

                subset.pop()
                arr[i] = False
            
        dfs([], ls)
        return res
            


            
        