class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(index, total):
            if total == target:
                res.append(subset.copy())

            for i in range(index, len(nums)):
                if total + nums[i] > target:
                    return
                subset.append(nums[i])
                dfs(i, total + nums[i])
                subset.pop()
        
        dfs(0,0)
        return res