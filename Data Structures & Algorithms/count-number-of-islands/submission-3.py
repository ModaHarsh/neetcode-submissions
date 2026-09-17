class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## solution using breadth first search
        ## okay so basically for each encountered island 
        ## first you are teling me to 
        ## append (to q) and sink all its neighbouring islands
        ## and then when the que is empty bfs for the initial land encountered
        ## is over we increase island count
    
        totalRows, totalCols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1,0], [-1, 0]]
        islandCount = 0

        def bfs(row, col):
            q = deque()
            grid[row][col] = '0'
            q.append((row, col))

            while q:
                curRow, curCol = q.popleft()
                for dr, dc in directions:
                    Row, Col = curRow + dr, curCol + dc
                    
                    if ( (Row < 0) or (Row >= totalRows) or 
                    (Col < 0) or (Col >= totalCols) or 
                    grid[Row][Col] == '0'):
                        continue
                    
                    grid[Row][Col] = '0'
                    q.append((Row,Col))
            
        for r in range(totalRows):
            for c in range(totalCols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islandCount += 1

        return islandCount
                    