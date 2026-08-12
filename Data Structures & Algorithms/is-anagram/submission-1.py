class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False        #diff no of characters
        
        x = sorted(s)
        y = sorted(t)
        for i in range(0, len(x)):
            if(x[i] != y[i]):
                return False        #every character in sorted array is the same
        return True

