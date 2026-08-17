class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
            elif s[r] in charSet:
                while(s[r] in charSet):
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
            res = max(res, r - l + 1)
        return res