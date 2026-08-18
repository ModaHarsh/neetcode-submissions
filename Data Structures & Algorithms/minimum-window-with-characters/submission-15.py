class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tMap = {}  # small
        sMap = {}  # big

        if len(s) < len(t):
            return ""

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        need,have = len(tMap), 0

        string = ""
        l = 0
        flag = 0
        min = len(s) + 1

        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            
            if (s[r] in tMap) and sMap[s[r]] == tMap[s[r]]:
                have += 1

            if (have == need):
                # we finally get the set then now
                flag = 1
                ## we need to figure out checking algorithm this is too complex

                while (have == need):
                    if (r - l + 1) < min:
                        min = r - l + 1
                        L = l
                        R = r

                    if sMap[s[l]] == 1:
                        if s[l] in tMap:
                            have -= 1 
                        del sMap[s[l]]
    
                    elif sMap[s[l]] != 1:
                        sMap[s[l]] -= 1
                        
                        if (s[l] in tMap) and (sMap[s[l]] < tMap[s[l]]):
                            have -= 1
                                           
                    l += 1

        if flag == 0:
            return ""

        return s[L : R + 1]
