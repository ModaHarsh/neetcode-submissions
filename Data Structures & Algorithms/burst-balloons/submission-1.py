class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ## okay so basically at every level we can either choose 
        ## to burst a balloon or we can choose to not burst the balloon
        ## trying hashMap approach first and then will go for
        ## 2dimensional space approach
        hashMap = {}

        def rec(i, nums):
            if not nums:
                return 0
            
            if i == len(nums):
                return 0
            
            if (i, tuple(nums)) in hashMap:
                return hashMap[(i, tuple(nums))]

            L = nums[i - 1] if i - 1 >= 0 else 1
            R = nums[i + 1] if i + 1 < len(nums) else 1
            
            burst = L * nums[i] * R
            numsCopy = nums.copy()
            numsCopy.pop(i)

            hashMap[(i, tuple(nums))] = max(burst + rec(0, numsCopy), rec(i + 1, nums))
            return hashMap[(i, tuple(nums))]
               
        return rec(0, nums)
