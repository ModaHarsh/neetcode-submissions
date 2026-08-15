class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(0,len(nums)-1):
            l = i + 1
            r = len(nums)-1
            if (i>0) and (nums[i] == nums[i-1]):
                continue
            
            while(l<r):
                s = nums[l] + nums[r] + nums[i]
                if (s < 0):
                    l += 1
                elif (s > 0):
                    r -= 1
                else:
                    temp = [nums[l], nums[r], nums[i]]
                    temp.sort()
                    if temp not in arr:
                        arr.append(temp)
                    while ((l<r) and (nums[l] == nums[l + 1])):
                        l += 1
                    while ((l<r) and (nums[l] == nums[r - 1])):
                        r -= 1
                    l += 1
                    r -= 1
        return arr
                    
        