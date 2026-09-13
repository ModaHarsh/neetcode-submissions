class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ## we will work with lists
        ## and then covert it to our desired O/P format
        if n == 1:
            return [["Q"]]
        board = [[0 for _ in range(n)] for _ in range(n)]     ## board[row][coloumn]
        def qcheck(r,c,board):
            for row in range(0,n):
                if board[row][c] == 1:
                    return False
            
            for col in range(0,n):
                if board[r][col] == 1:
                    return False
                
            row, col = r, c        ## priciple diagonal
            while(0<= row and 0<= col):
                row -= 1
                col -= 1
            row += 1
            col += 1
            while(row < n and col < n):
                if board[row][col] == 1:
                    return False
                row += 1
                col += 1
            
            row, col = r, c         ## the other diagonal
            while (row >= 0 and col < n):
                row -= 1
                col += 1 
            row += 1
            col -= 1

            while (row < n and col >= 0):
                if board[row][col] == 1:
                    return False
                row += 1
                col -= 1
            return True
        # board = [[0 for _ in range(n)] for _ in range(n)]
        validBoards = []
        def dfs(row, board):
            if row == n:
                validBoards.append([row[:] for row in board])
                return
            
            for col in range(n):                ## basically n queens 
                if qcheck(row, col, board):     ## which will be placed in n rows and cols
                    board[row][col] = 1         ## so every row will have a queen
                    dfs(row + 1, board)         ## by common logic so we do thiss instead
                    board[row][col] = 0         ## of previous solution


        dfs(0, board)
        res = []
        for b in validBoards:
            board = ["" for _ in range(n)]
            for row in range(0,n):
                for col in range(0,n):
                    if b[row][col] == 1:
                        board[row] += "Q"
                    if b[row][col] == 0:
                        board[row] += "."
            res.append(board.copy())
        return res

