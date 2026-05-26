class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        total = 0
        res = []
        subset = []

        def dfs(index):
            nonlocal total
            if total == target:
                res.append(subset.copy())
            elif total > target:
                return

            for i in range(index, len(nums)):
                subset.append(nums[i])
                total += nums[i]
                dfs(i)
                subset.pop()
                total -= nums[i]
        
        dfs(0)
        return res