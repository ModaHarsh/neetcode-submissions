class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in range(0, len(nums)):
            product = product * nums[i]
        
        output = [0] * len(nums)
        for i in range(0, len(nums)):
            if nums[i] == 0:
                prod = 1
                for j in range(0,len(nums)):
                    if j == i:
                        continue
                    prod = prod * nums[j]
                output[i] = prod
            else:
                output[i] = product/nums[i]
            output[i] = int(output[i])
        return output

