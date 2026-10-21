class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        totalRows = m
        totalCols = n

        grid = [[0] * n for _ in range(m)]

        def dfs(row, col):

            if row >= totalRows or col >= totalCols:
                return 0

            if (row == totalRows - 1) and (col == totalCols - 1):
                return 1
            
            if grid[row][col] != 0:
                return grid[row][col]

            grid[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return grid[row][col]
        
        return dfs(0 , 0)