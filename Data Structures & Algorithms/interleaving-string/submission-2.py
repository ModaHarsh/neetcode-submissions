class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        ## we will keep three pointers i, j and k 
        ## i -- s1
        ## j -- s2
        ## k -- s3
        ## k == i + j
        hashMap = {}

        def rec(i, j, k):
            if (i ,j) in hashMap:
                return hashMap[(i, j)]
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            if k == len(s3):
                return False

            if j < len(s2) and i < len(s1) and s3[k] == s2[j] and s3[k] == s1[i]:
                left = rec(i + 1, j, k + 1)
                right = rec(i, j + 1, k + 1)
                hashMap[(i, j)] = left or right
                return hashMap[(i , j)]
            
            if j < len(s2) and s3[k] == s2[j]:
                hashMap[(i, j)] = rec(i, j + 1, k + 1)
                return hashMap[(i , j)]

            if i < len(s1) and s3[k] == s1[i]:
                hashMap[(i, j)] = rec(i + 1, j, k + 1)
                return hashMap[(i , j)]
            
        if rec(0,0,0):
            return True
        else: return False