class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        def dfs(index, subset):
            if index >= len(nums):
                res.add(tuple(subset[:]))
                return
            
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()
            dfs(index + 1, subset)
        
        dfs(0,[])

        return list(res)