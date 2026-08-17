class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        
        l, res = 0,0
        
        for r in range(len(s)):
         #length of substring

            if s[r] not in map:
                map[s[r]] = 1
            else:
                map[s[r]] += 1
            
           #max freq of element in substring           

            while(k < ((r - l + 1) - max(map.values()))):
                map[s[l]] -= 1
                l += 1

            # checking condtions if (l to r) satisfies our conditions
            # or shift l till it satisfies condition

            L = (r - l + 1)
            res = max(res, L)

            # reduce window size if K = (L - maxFreqOfElement(substring))
            # reduce window size by 1 that too
        return res
            



        