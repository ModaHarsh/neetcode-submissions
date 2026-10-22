class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ## let rec(i , j) return the no of operations needed
        ## to change word1 to word2 at w1 from index i and 
        ## w2 at index j
        grid = [[-1] * len(word2) for _ in range(len(word1))]
        def rec(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return 1 + rec(i, j + 1)    ## inserting elements
            if j == len(word2):
                return 1 + rec(i + 1, j)    ## deleting elements
            
            if grid[i][j] != -1:
                return grid[i][j]
            
            if word1[i] == word2[j]:
                grid[i][j] =  rec(i + 1, j + 1)

            if word1[i] != word2[j]:
                delete = 1 + rec(i + 1, j)
                replace = 1 + rec(i + 1, j + 1)
                insert = 1 + rec(i, j + 1)
                grid[i][j] =  min(delete, replace, insert)
            
            return grid[i][j]
        
        return rec(0, 0)