class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset):  # we will be writing some recursive code here
            if i == len(nums):
                res.append(subset.copy())   ## if we don't use copy it will store a
                                            ## referance or like a pointer to the subset object
                                            ## which at the decision tree branch will point to a
                                            ## completely empty object
                return 
            
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()

            dfs(i + 1, subset)
        dfs(0, [])
        return res
