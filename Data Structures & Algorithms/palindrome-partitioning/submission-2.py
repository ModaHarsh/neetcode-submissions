class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPal(t):
            i, j = 0, len(t) -1 
            while(i <= j):
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(start, l):
            if start == len(s):
                res.append(l.copy())
                return
            
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if isPal(piece):
                    l.append(piece)
                    dfs(end, l)
                    l.pop()

        dfs(0, [])
        return res