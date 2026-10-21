class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ## can solve using recursion
        hashMap = {}

        def rec(i, amount):
            if (i , amount) in hashMap:
                return hashMap[(i, amount)]
            if i == len(nums) and amount == target:
                return 1
            if i == len(nums) and amount != target:
                return 0
            
            add = rec(i + 1, amount + nums[i])
            sub = rec(i + 1, amount - nums[i])
            hashMap[(i, amount)] = add + sub
            return hashMap[(i, amount)]
        
        return rec(0, 0)