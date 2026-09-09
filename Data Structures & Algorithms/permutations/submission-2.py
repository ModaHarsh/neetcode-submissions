class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = [False] * len(nums)
        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if curr[i]:
                    continue
                
                curr[i] = True
                subset.append(nums[i])
                
                dfs(subset)

                curr[i] = False
                subset.pop()
        dfs([])
        return res