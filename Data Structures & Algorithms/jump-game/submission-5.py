class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## can solve using simple recursion
        cache = [None] * len(nums)

        def rec(i):
            if i == len(nums) - 1:
                return True

            if i >= len(nums):
                return False

            if cache[i] != None:
                return cache[i]

            if nums[i] == 0:
                cache[i] = False
                return cache[i]

            for steps in range(1, nums[i] + 1):
                if rec(i + steps):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return cache[i]

        return True if rec(0) else False