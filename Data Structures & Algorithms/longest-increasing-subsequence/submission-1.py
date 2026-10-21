class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        j = -1
        
        hashMap = {}

        def rec(i, j):
            if (i, j) in hashMap:
                return hashMap[(i, j)]

            if i == len(nums):
                return 0

            if j == -1 or nums[i] > nums[j]:
                hashMap[(i, j)] = max(rec(i + 1, j), 1 + rec(i + 1, i))
                return hashMap[(i, j)]
            
            else:
                hashMap[(i, j)] = rec(i + 1, j)
                return hashMap[(i, j)]
        
        return rec(0, -1)