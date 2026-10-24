class Solution:
    def jump(self, nums: List[int]) -> int:
        ## two pointers 
        ## l and r representing the range
        ## of reachable indices
        ##

        l = 0
        r = 0
        steps = 0
        while(r < len(nums) - 1):       ## end of staircase still not in reach/range
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            steps += 1
        return steps