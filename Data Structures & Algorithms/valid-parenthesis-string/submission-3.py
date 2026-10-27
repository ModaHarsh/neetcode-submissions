class Solution:
    def checkValidString(self, s: str) -> bool:
        ## correct more standard approach
        hi, lo = 0, 0
        ## they track highest and lowest 
        ## number of open brackets ( possible at a point
        ## in the string


        for c in s:
            if c == "(":
                hi += 1
                lo += 1
            if c == ")":
                hi -= 1
                lo -= 1
            
            if c == "*":
                hi += 1
                lo -= 1
            
            if lo < 0:
                lo = 0      ## we can turn the asterisk as nothing aswell
            
            if hi < 0:      ## more right brackets from left to right scan
                return False

        return lo == 0