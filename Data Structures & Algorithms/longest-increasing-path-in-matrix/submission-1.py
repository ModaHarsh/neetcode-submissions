class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        grid = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        
        def rec(row , col):
            if grid[row][col] != -1:
                return grid[row][col]

            up = 1
            down = 1
            left = 1
            right = 1

            if row - 1 >= 0 and matrix[row - 1][col] > matrix[row][col]:
                up = 1 + rec(row - 1, col)
            if row + 1 < len(matrix) and matrix[row + 1][col] > matrix[row][col]:
                down = 1 + rec(row + 1, col)
            if col - 1 >= 0 and matrix[row][col - 1] > matrix[row][col]:
                left = 1 + rec(row, col - 1)
            if col + 1 < len(matrix[0]) and matrix[row][col + 1] > matrix[row][col]:
                right = 1 + rec(row, col + 1)
            
            grid[row][col] = max(up, down, left, right)
            return grid[row][col]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                rec(i , j)
        
        res = -1 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, grid[i][j])

        return res 