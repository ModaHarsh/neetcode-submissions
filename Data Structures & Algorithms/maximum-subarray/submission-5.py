class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ## rec(i) returns sum of largest subarray from 
        ## index i to n-1
        ## so final answer should just be given by 
        ## rec(0)
        
        hashMap = {}

        def rec(i, started):
            if i == len(nums):
                return 0 if started else float("-inf")
            
            if (i, started) in hashMap:
                return hashMap[(i, started)]

            if started:
                end = 0
                take = nums[i] + rec(i + 1, True)
                hashMap[(i, started)] = max(end, take)

            else:
                start = nums[i] + rec(i + 1, True)
                skip = rec(i + 1, False)
                hashMap[(i, started)] = max(start, skip)
            
            return hashMap[(i, started)]
        
        return rec(0, False)