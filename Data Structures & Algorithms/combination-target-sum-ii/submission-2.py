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
            
            seen = set()
            
            for i in range(index, len(candidates)):
                if candidates[i] in seen:
                    continue
                if total + candidates[i] > target:
                    break
                seen.add(candidates[i])
                subset.append(candidates[i])
                dfs(i+1, total + candidates[i], subset)
                subset.pop()
            
        dfs(0,0,[])
        return res
        