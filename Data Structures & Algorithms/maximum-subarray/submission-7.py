class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## trying to solve in just one scan
        ## called kadane's algorithm 
        ## use to find maximum sum subarray
        ## in a list
        curSum = 0
        res = nums[0]
        for i in range(len(nums)):
            curSum += nums[i]
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
        
        return res