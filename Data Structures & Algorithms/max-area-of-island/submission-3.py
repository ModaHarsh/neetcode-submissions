class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ## solving using bfs approach
        
        totalRows, totalCols = len(grid), len(grid[0])
        dirn = [[0, 1] ,[0, -1], [1,0] , [-1, 0]]
        res = 0
        
        def bfs(row, col):
            nonlocal res
            count = 1
            res = max(count , res)

            grid[row][col] = 0
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in dirn:
                    
                    nr, nc = r + dr, c + dc
                    
                    if ((nr < 0) or (nr >= totalRows) or
                    (nc < 0) or (nc >= totalCols) or 
                    grid[nr][nc] == 0):
                        continue
                    
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    count += 1
                    res = max(res, count)
        
        
        
        for r in range(totalRows):
            for c in range(totalCols):
                if grid[r][c] == 1:
                    bfs(r, c)
        return res
