class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ## can be solved using recursion
        ## at each step we can either choose an alphabet
        ## or we can leave it
        hashMap = {}

        def rec(i, text):
            if (i, text) in hashMap:
                return hashMap[(i, text)]

            if text == t:
                return 1
            
            if i == len(s):
                return 0
            
            take = rec(i + 1, text + s[i])
            leave = rec(i + 1, text)

            hashMap[(i, text)] = take + leave
            return hashMap[(i, text)]
        
        return rec(0, "")