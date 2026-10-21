class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        halfSum = totalSum / 2
        
        hashMap = {}

        def rec(i, curSum):
            if (i, curSum) in hashMap:
                return hashMap[(i, curSum)]

            if curSum == halfSum:
                return True
            
            if i == len(nums):
                return False
            
            if rec(i + 1, curSum + nums[i]):
                hashMap[(i, curSum)] = True
                return True
            if rec(i + 1, curSum):
                hashMap[(i, curSum)] = True
                return True
            
            hashMap[(i, curSum)] = False
            return False
        
        return rec(0, 0)