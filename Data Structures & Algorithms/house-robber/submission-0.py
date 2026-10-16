class Solution:
    def rob(self, nums: List[int]) -> int:
        hashMap = {}
        def dfs(n):
            if n >= len(nums):
                return 0
            if n in hashMap:
                return hashMap[n]
            
            hashMap[n] = max(nums[n] + dfs(n + 2), dfs(n + 1))
            return hashMap[n]
        
        return dfs(0)