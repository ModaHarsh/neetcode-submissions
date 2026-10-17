class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## best palindrome found so far
        resIdx, resLen = 0, 0
        n = len(s)

        ## dp[i][j] = is s[i: j + 1] a plindrome?
        dp = [[False] * n for _ in range(n)]

        ## processing starting positions from right to left
        for i in range(n - 1, -1, -1):

            ## every ending position j >= i
            for j in range(i, n):

                if s[i] == s[j] and ((j - i) <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = (j - i + 1)
        
        return s[resIdx: resIdx + resLen]
