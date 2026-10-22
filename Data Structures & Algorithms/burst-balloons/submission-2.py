class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        grid = [[-1] * len(nums) for _ in range(len(nums))]

        def rec(l , r): 
            if l + 1 == r:
                return 0
            
            if grid[l][r] != -1:
                return grid[l][r]

            best = -1
            for k in range(l + 1, r):
                best = max(best, rec(l, k) + nums[l] * nums[k] * nums[r] + rec(k, r))
            
            grid[l][r] = best
            return grid[l][r]
        
        return rec(0, len(nums) - 1)