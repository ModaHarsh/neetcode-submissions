class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ## using starting index and ending index approach
        startMap = {}
        for i in range(len(s)):
            if s[i] not in startMap:
                startMap[s[i]] = i

        endMap = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in endMap:
                endMap[s[i]] = i
        
        i = 0
        res = []
        while i < len(s):
            L = startMap[s[i]]
            R = endMap[s[i]]
            k = L
            while k <= R:
                if endMap[s[k]] > R:
                    R = endMap[s[k]]
                k += 1
            i = k
            res.append(R - L + 1)
        
        return res