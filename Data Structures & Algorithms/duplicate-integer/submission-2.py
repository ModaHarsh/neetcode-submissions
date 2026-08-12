class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)-1):
            x = nums[i]
            y = nums[i + 1]
            if (x == y):
                return True
        return False
