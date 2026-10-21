class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        grid = [[-1] * len(text2) for _ in range(len(text1))]


        def search(i, j):
            
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if grid[i][j] != -1:
                return grid[i][j]

            if text1[i] == text2[j]:
                grid[i][j] = 1 + search(i + 1, j + 1)
                return grid[i][j]
            
            grid[i][j] = max(search(i + 1, j), search(i, j + 1))
            return grid[i][j]

        return search(0,0)