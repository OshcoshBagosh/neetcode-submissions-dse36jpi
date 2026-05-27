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
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:  # skip duplicates
                    continue
                if total + candidates[i] > target:
                    return
                subset.append(candidates[i])
                dfs(i+1, total + candidates[i], subset)
                subset.pop()
            
        dfs(0,0,[])
        return res
        