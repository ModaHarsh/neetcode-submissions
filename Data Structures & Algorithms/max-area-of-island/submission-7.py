class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1,0], [-1,0]]
        
        def dfs(row, col):
            nonlocal count, res
            if (row < 0) or (row >= len(grid)):
                return 
            if (col < 0) or (col >= len(grid[0])):
                return 
            if grid[row][col] == 0:
                return

            if grid[row][col] == 1:
                grid[row][col] = 0
                count += 1
                
                res = max(res, count)
                for dr, dc in directions:
                    dfs(row + dr, col + dc)
        
        
        
        res = 0
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                count = 0
                dfs(i, k)

        return res