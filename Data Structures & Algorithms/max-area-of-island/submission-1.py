class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
    ## very similar to previous question
    ## trying with different direction code implementation
    ## approach dfs itself this too
    
        totalRow, totalCol = len(grid), len(grid[0])
        directions = [ [1,0], [-1, 0], [0, 1], [0, -1]]
    
        res = 0
        count = 0
        def dfs(row, col):
            nonlocal res
            nonlocal count
            nonlocal flag

            if ((row < 0) or (row >= totalRow) 
            or (col < 0) or (col >= totalCol) 
            or (grid[row][col] == 0)):
                return

            grid[row][col] = 0

            if flag == 0:
                flag = 1
                count = 0
        
            count += 1
        
            res = max(count, res)

            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                flag = 0
                dfs(r, c)
        return res