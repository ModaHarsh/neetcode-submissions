class Solution:
    def checkValidString(self, s: str) -> bool:
        leftCount = 0
        rightCount = 0
        asteriskCount = 0
        flag1 = 0

        for i in range(len(s)):
            if s[i] == "(":
                leftCount += 1
            if s[i] == ")":
                rightCount += 1
            if s[i] == "*":
                asteriskCount += 1
            
            if rightCount > leftCount + asteriskCount:
                return False
        
        if asteriskCount >= rightCount - leftCount:
            flag1 = 1
        
        leftCount = 0
        rightCount = 0
        asteriskCount = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                leftCount += 1
            if s[i] == ")":
                rightCount += 1
            if s[i] == "*":
                asteriskCount += 1
            
            if leftCount > rightCount + asteriskCount:
                return False
        
        return True if flag1 else False

        
