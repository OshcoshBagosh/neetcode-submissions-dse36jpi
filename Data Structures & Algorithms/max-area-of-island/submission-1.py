class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row, col):
            if grid[row][col] == 0:
                return 0

            #mark as visted
            grid[row][col] = 0

            area = 1

            for v1, v2 in moves:
                r, c = row + v1, col + v2
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                    continue

                area += dfs(r,c)

            return area
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                max_area = max(max_area, dfs(row,col))
        
        return max_area

        