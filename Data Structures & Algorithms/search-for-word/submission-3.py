class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        We loop through 2d array until we hit a char that equals
        word[0]
        Then we use dfs to find a path that equals word
        """
        n, m = len(board), len(board[0])

        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col, index, visited=None):
            #A set to ignore past visited coords
            if not visited:
                visited = set()
            if index == len(word)-1:
                return True
            #Goes through every possible move
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
