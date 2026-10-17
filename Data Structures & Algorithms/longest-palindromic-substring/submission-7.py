class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]


        resLen = 0
        for i in range(len(s)):
            
            if (i + 1) == len(s):
                continue

            L, R = i, (i + 1)
            while((L >= 0) and (R < len(s)) and (s[L] == s[R])):
                resLen = max(resLen, R - L + 1)
                if resLen == (R - L + 1):
                    res = s[L : R + 1]
                L -= 1
                R += 1

            if (i - 1) < 0:
                continue

            L, R = (i - 1), (i + 1)
            while((L >= 0) and (R < len(s)) and (s[L] == s[R])):
                resLen = max(resLen, R - L + 1)
                if resLen == (R - L + 1):
                    res = s[L:R + 1] 
                L -= 1
                R += 1
            
            
        if resLen == 0:
            return s[0]

        return res