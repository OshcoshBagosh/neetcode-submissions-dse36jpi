class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        What we know is that Os on the border will not be surronded
        So we can apply dfs to find rest Os in the group
        """
        ROW, COL = len(board), len(board[0])

        def dfs(row, col):
            if 0 < row >= ROW or 0 < col >= COL or board[row][col] != 'O':
                return
            
            #set it to a # to mark as visited
            board[row][col] = '#'

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        #Horizontal borders 
        for i in range(COL):
            if board[0][i] == 'O': 
                dfs(0, i)
            if board[ROW-1][i] == 'O': 
                dfs(ROW-1, i)

        #Vertical borders
        for i in range(1,ROW-1):
            if board[i][0] == 'O': 
                dfs(i, 0)
            if board[i][COL-1] == 'O': 
                dfs(i, COL-1)
        
        #Convert #s back to Os and Os to Xs
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
        
        