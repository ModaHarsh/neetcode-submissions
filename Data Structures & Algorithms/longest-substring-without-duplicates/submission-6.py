class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0,0

        for r in range(len(s)):
            # if R in set shift L till its removed from set and then add R            
            # if R not in set add it

            # after ever new element is added we check the length of the string
            while(s[r] in charSet):
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
