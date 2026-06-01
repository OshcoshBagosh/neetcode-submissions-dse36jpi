class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col, index, visited=None):
            if not visited:
                visited = set()
            if index == len(word)-1:
                return True

            for v1, v2 in moves:
                r,c = row + v1, col + v2
                if r < 0 or r >= n or c < 0 or c >= m:
                    continue
                if board[r][c] != word[index+1] or (r,c) in visited:
                    continue
                print(f"{board[r][c]}: {word[index+1]}")
                print((r,c))
                visited.add((row,col))
                if dfs(r, c, index + 1, visited):
                    return True
                visited.remove((row,col))

        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        
        return False
