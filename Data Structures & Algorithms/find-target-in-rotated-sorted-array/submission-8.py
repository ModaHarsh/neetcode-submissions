class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while (l < r):
            m = (l + r) // 2

            if (target == nums[m]):
                return m
            if (target == nums[l]):
                return l
            if (target == nums[r]):
                return r
            if (l + 1) == r:
                break
            
            if (nums[l] < nums[m]) and (target < nums[m]) and (target >= nums[l]):
                r = m - 1
                l += 1
                break
            elif (nums[l] < nums[m]):
                l = m + 1
            
            elif (nums[m] < nums[r]) and (target > nums[m]) and (target <= nums[r]):
                l = m + 1
                r -= 1
                break
            
            elif(nums[m] < nums[r]):
                r = m - 1
            

            
            

        while(l <= r):
            m = (l + r) // 2
            if (nums[m] > target):
                r = m - 1
            elif (nums[m] < target):
                l = m + 1
            else:
                return m
        
        return -1
