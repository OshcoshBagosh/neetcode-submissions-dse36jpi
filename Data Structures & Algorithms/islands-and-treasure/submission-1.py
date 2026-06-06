class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False] * COLS for i in range(ROWS)]
            visit[r][c] = True
            count = 0
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return count
                    for mr, mc in moves:
                        nr, nc = row + mr, col + mc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and
                            not visit[nr][nc] and grid[nr][nc] != -1
                        ):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                count += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)