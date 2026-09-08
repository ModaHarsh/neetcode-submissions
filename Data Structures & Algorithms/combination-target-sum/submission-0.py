class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        totalLength = target // min(nums)
        def dfs(i, subset):
            if i == len(nums):
                return 
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if len(subset) > totalLength:
                return 
            if sum(subset) > target:
                return
            
            subset.append(nums[i])
            dfs(i, subset)
            subset.pop()
            dfs(i + 1, subset)
        
        dfs(0, [])
        return res
