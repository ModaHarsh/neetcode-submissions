class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ## solving using dfs approach
        ## needing to use stack instead of recursion
        
        directions = [[0, 1], [1,0], [0, -1],[-1,0]]
        totalRows = len(board)
        totalCols = len(board[0])
        stack = []
        
        def dfs(row, col):
            nonlocal flag, visit
            stack.append((row, col))
            
            
            while stack:
                curRow, curCol = stack.pop()
                visit.add((curRow, curCol))

                if ( (curRow == 0) or (curCol == 0) or (curRow == (totalRows-1)) or
                (curCol == (totalCols - 1))):
                    flag = 1
            
            
                for dr, dc in directions:
                    dR, dC = curRow + dr, curCol + dc
                    
                    if ((0 <= dR < totalRows) and (0 <= dC < totalCols)
                    and ((dR, dC) not in visit) and (board[dR][dC] == "O")):
                        
                        stack.append((dR, dC))

        leftout = set()
        for i in range(len(board)):
            for k in range(len(board[0])):
                
                if board[i][k] == "O":
                    
                    if (i,k) in leftout:
                        continue
                    
                    flag = 0
                    visit = set()
                    dfs(i ,k)
                    
                    if flag == 0:
                        for r, c in visit:
                            board[r][c] = "X"
                    if flag == 1:
                        for j in visit:
                            leftout.add(j)


