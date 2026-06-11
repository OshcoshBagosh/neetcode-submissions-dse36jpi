class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        l_max, r_max = heights[l], heights[r]
        res = 0

        while l < r:
            area = min(l_max, r_max) * (r - l)
            res = max(res, area)

            if l_max < r_max:
                l += 1
                l_max = max(l_max, heights[l])
            else:
                r -= 1
                r_max = max(r_max, heights[r])
        
        return res
        