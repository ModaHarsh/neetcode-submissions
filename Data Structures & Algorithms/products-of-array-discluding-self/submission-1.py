class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ''' maybe using two arrays before and after
            containing product of the elements of the array before & 
            after ith element in the array'''
            
        prefix = [0] * len(nums)
        prefix[0] = 1
        prefix[1] = nums[0]
        for i in range(2,len(nums)):
           prefix[i] = prefix[i-1] * nums[i-1]

        n = len(nums)
        suffix = [0] * len(nums)
        suffix[n-1] = 1
        suffix[n-2] = nums[n-1]
        for i in range(len(nums)-3,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        output = [0] * len(nums)
        for i in range(0,len(nums)):
            output[i] = prefix[i] * suffix[i]
        return output


