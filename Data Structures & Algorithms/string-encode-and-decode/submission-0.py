class Solution:

    def encode(self, strs: List[str]) -> str:
        # we can use (num)# as an identifier where num is the length of 
        # the string and hashtag works as a separator so length does not get 
        # mixed with the actual string
        masterString = ""
        for i in range(0, len(strs)):               #iterating through strings
            num = len(strs[i])                      #len of i'th string
            masterString += str(num) + "#"  
            for j in range(0,len(strs[i])):
                masterString += strs[i][j] 
    
        return masterString;
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i < len(s)):
            length = "";
            while (s[i] != "#"):
                length += s[i]
                i += 1
            length = int(length)
            string = ""
            i += 1                  #moving i from hash to string
            j = i
            for j in range(j, j+length):
                string += s[j]
            res.append(string)
            i += length
        return res
                

        


