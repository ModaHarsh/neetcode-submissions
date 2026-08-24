class Solution:
    def findMin(self, nums: List[int]) -> int:
        # skeched out algorithm on notebook works to find the max element of the arr
        # if we find the max, min is just the next element then

        l = 0
        r = len(nums) - 1
        if(nums[l] < nums[r]) or (len(nums) == 1):
            return nums[l]
        

        while True:
            mid = int((r + l)/2)
            
            if(nums[mid - 1] > nums[mid]):
                return nums[mid]
            
            if (nums[mid] == nums[l]):
                maxIndex = mid
                break
            elif (nums[l] > nums[mid]):      #rotation break is on left of mid
                r = mid 
            elif (nums[r] < nums[mid]):     #rotation break is on rigth of mid
                l = mid 

            
        
        return nums[maxIndex + 1]
        

                
