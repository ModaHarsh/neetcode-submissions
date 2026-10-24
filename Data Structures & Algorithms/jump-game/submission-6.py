class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## can also be solved using a greedy approach
        ## in one scan by keeping a track of the furthest 
        ## reachable index
        curMax = nums[0]
        for i in range(len(nums)):
            if i > curMax:
                return False
            if i == len(nums) - 1:
                return True
            if i + nums[i] > curMax:
                curMax = i + nums[i]