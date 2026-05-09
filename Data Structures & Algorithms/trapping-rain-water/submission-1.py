class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        max_left = []
        max_right = collections.deque()
        area = 0
        for i in range(len(height)):
            if i-1 < 0:
                max_left.append(0)
            else:
                l = max(l, height[i-1])
                max_left.append(l)
        for i in range(len(height)-1, -1, -1):
            if i+1 >= len(height):
                max_right.append(0)
            else:
                r = max(r, height[i+1])
                max_right.appendleft(r)
        for i in range(len(height)):
            total = min(max_left[i], max_right[i]) - height[i]
            if total > 0:
                area += total
        
        return area