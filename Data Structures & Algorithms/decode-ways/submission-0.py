class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        hashMap = {}  
        def rec(i):
            if i == n:
                return 1
            if i in hashMap:
                return hashMap[i]



            left = 0
            right = 0

            
            if int(s[i]) != 0:
                left = rec(i + 1)

            if int(s[i]) != 0 and (i + 1) < n and int(s[i: i + 2]) <= 26:
                right = rec(i + 2)

            hashMap[i] = left + right
            return hashMap[i]
         
        return rec(0)