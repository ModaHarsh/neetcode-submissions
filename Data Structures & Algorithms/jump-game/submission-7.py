class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## second greedy apporach
        ## backwards scan
        ## keeping of the rightmost element which can reach our goal
        ## goal keeps updating

        goal = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0