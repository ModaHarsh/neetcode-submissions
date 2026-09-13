class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = {2:'abc', 3:'def', 4:'ghi', 
        5:'jkl', 6:'mno', 7:'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        if len(digits) == 0:
            return []

        def dfs(i, text):
            if i == len(digits):
                res.append(text[:])
                return
            
            d = int(digits[i])
            for c in digitMap[d]:
                dfs(i + 1, text + c)

        dfs(0,'')
        return res