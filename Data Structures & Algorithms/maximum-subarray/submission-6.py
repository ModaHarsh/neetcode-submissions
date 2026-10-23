class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## okay trying diff approach

        ## let rec(i) return the max sub of a substring which
        ## can be started from index i
        hashMap = {}
        def rec(i):
            if i == len(nums):
                return 0

            if i in hashMap:
                return hashMap[i]

            hashMap[i] = nums[i] + max(0, rec(i + 1))
            return hashMap[i]

        res = float("-inf")

        for i in range(len(nums)):
            res = max(res, rec(i))
        return res    