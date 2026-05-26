class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #We sort candidates to prevent us from looking at larger elements when over target
        candidates.sort()

        def dfs(index, total, subset):
            if total == target:
                #copy() is O(n)
                res.append(subset.copy())
                return
            if total > target or index == len(candidates):
                return

            subset.append(candidates[index])
            dfs(index+1, total + candidates[index], subset)
            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index + 1, total, subset)
            
        dfs(0,0,[])
        return res
        