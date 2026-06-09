class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        minutes = 0
        fresh = 0
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        while queue:
            if fresh == 0:
                return minutes
            minutes += 1
            print(grid)
            print(minutes)
            for i in range(len(queue)):
                r, c = queue.popleft()     
                
                for mr, mc in moves:
                    nr, nc = r + mr, c + mc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
                    fresh -= 1


        if fresh > 0:
            return -1

        return minutes
        """
            211 221 222 222 222
            110 210 220 220 220
            011 011 011 021 022
        """
        


        

        