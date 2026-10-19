class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = res
        curMin = res
        

        for i in range(1, len(nums)):
            candidates = (nums[i], curMax * nums[i], curMin * nums[i])
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(res, curMax)
        
        return res