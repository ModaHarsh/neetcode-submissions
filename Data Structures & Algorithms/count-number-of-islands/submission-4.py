class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## after midsem after coming back home try
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            nonlocal count
            nonlocal flag
            if (row >= len(grid)) or (col >= len(grid[0])) or (row < 0) or (col < 0) :
                return
            if (grid[row][col] == "0"):
                return 
            
            if grid[row][col] == "1":
                if flag == 0:
                    flag = 1
                    count += 1
                grid[row][col] = "0"
                for dr, dc in directions:
                    dfs(row + dr, col + dc)

        
        count = 0
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                flag = 0
                dfs(i, k)
        return count
