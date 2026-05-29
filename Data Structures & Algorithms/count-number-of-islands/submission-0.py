class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        moves = [(1,0), (-1,0), (0, 1), (0, -1)]
        def bfs(cord):
            from collections import deque
            queue = deque()
            queue.append(cord)
            while queue:
                row, col = queue.popleft()
                visited.add((row,col))
                for r, c in moves:
                    nr, nc = row + r, col + c
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    if (nr,nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr,nc))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs((row, col))
                    islands += 1
        
        return islands
        