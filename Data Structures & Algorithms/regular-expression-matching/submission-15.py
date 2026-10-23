class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ## can be solved using recursion
        ## s ---> i
        ## p ---> j
        grid = [[-1] * len(p) for _ in range(len(s) + 1)]

        def rec(i, j):
            
            if i == len(s) and j == len(p):
                return True

            if j == len(p) and i != len(s):
                return False

            if grid[i][j] != -1:
                return grid[i][j]

            if p[j] == "*":
                ends = rec(i, j + 1)
                none = rec(i - 1, j + 1)
                if (i < len(s)) and (p[j - 1] == s[i] or p[j - 1] == "."):
                    move = rec(i + 1, j + 1)
                    stay = rec(i + 1, j)
                    grid[i][j] = ends or none or move or stay
                    return grid[i][j]
                grid[i][j] = ends or none
                return grid[i][j]

            if i < len(s) and s[i] == p[j]:
                grid[i][j] = rec(i + 1, j + 1)
                return grid[i][j]
            
            if i < len(s) and p[j] == ".":
                grid[i][j] = rec(i + 1, j + 1)
                return grid[i][j]
            
            if j + 1 < len(p) and p[j + 1] == "*":
                grid[i][j] = rec(i, j + 2)
                return grid[i][j]
            
            grid[i][j] = False
            return grid[i][j]
        
        
        return rec(0,0)
        
