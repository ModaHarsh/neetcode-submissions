class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(row, col):
            nonlocal flag
            nonlocal count
            if grid[row][col] == "#":
                return
            if grid[row][col] == "0":
                return
            if grid[row][col] == "1":
                if flag == 0:
                    count += 1
                    flag = 1
                grid[row][col] = "#"
                if row != len(grid) - 1:   # going down
                    dfs(row + 1, col)
                if row != 0:
                    dfs(row - 1, col)       # going up
                if col != len(grid[0]) - 1: 
                    dfs(row, col + 1)       # going right
                if col != 0:
                    dfs(row, col - 1)       # going left
            
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                flag = 0
                dfs(i, k)

        return count