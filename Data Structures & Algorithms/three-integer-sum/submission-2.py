class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## sorting
        for i in range(1,len(nums)):
            if (nums[i] < nums[i-1]):
                j = i
                while ((j >= 1) and (nums[j] < nums[j-1])):
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
                    j -= 1
        
        # sorted now
        arr = []
        for i in range(0,len(nums)-2):
            l,r = i + 1, len(nums)-1

            if (i>0 and nums[i] == nums[i-1]):
                continue
            while(l<r):
                s = nums[i] + nums[l] + nums[r]
                if(s<0):
                    l += 1
                elif(s>0):
                    r -= 1
                else:
                    arr.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
        return arr





'''            l,r = 0, len(nums)-1
            if nums[l] + nums[r] < -nums[i]:
                while l < i:
                    l += 1
                    if (nums[l] + nums[r] == -nums[i]) and ([nums[l] , nums[i], nums[r]] not in arr):
                        arr.append([nums[l] , nums[i], nums[r]])
            elif nums[l] + nums[r] > -nums[i]:
                while r > i:
                    r -= 1
                    if (nums[l] + nums[r] == -nums[i]) and ([nums[l] , nums[i], nums[r]] not in arr):
                        arr.append([nums[l] , nums[i], nums[r]])
            elif [nums[l] , nums[i], nums[r]] not in arr:
                arr.append([nums[l] , nums[i], nums[r]])
        return arr      
        
        
        if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            
            while(l<r):
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    arr.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                break
        return arr'''
                



