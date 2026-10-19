class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        hashMap = {}

        def dfs(i):
            if i in hashMap:
                return hashMap[i]
            
            if i == len(s):
                return True


            for word in wordDict:
                flag = 0
                if len(word) > (len(s) - i):
                    continue

                for c in range(len(word)):
                    if word[c] != s[i + c]:
                        flag = 1
                        break
                
                if flag == 1:
                    continue

                if dfs(i + len(word)):
                    hashMap[i] = True
                    return True
            
            hashMap[i] = False
            return False

        if dfs(0):
            return True
        else: return False