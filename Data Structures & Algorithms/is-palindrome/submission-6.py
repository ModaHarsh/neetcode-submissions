class Solution:
    def isPalindrome(self, s: str) -> bool:
        strList = []
        for i in range(0,len(s)):
            if s[i].isalnum():
                strList.append(s[i].lower())
        
        for i in range(0, int(len(strList)/2)):
            if strList[i] != strList[len(strList)-1-i]:
                return False
        return True


        