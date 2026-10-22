class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ## improving on complexity
        ## can be solved using recursion
        ## i --> s 
        ## j --> t
        
        grid = [[-1] * len(t) for _ in range(len(s))]
        
        ## rec(i, j) returns the no of ways t can be formed starting
        ## from index i of s and from till when index j of t
        ## is already formed/acquired

        ## hence rec(0,0) will return no of ways of forming 
        ## t from s choosing and skipping elements

        def rec(i , j):
            
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if grid[i][j] != -1:
                return grid[i][j]

            if t[j] == s[i]:
                take = rec(i + 1, j + 1)
                leave = rec(i + 1, j)
                grid[i][j] = take + leave
                return grid[i][j]

            else:
                leave = rec(i + 1, j)
                grid[i][j] = leave
                return grid[i][j]

        return rec(0, 0)        