class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Undo the choice
            subset.pop()

            # Don't include nums[i]
            backtrack(i + 1, subset)

        backtrack(0, [])

        return res