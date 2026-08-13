class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        startingValues = []
        for n in nums:
            if (n-1 not in numSet):
                startingValues.append(n)
        
        counter = [1] * len(startingValues)
        for i in range(0, len(startingValues)):
            y = startingValues[i]       # y = starting value itself
            while y+1 in numSet:
                counter[i] += 1
                y += 1
        
        max = 0
        for k in range(0, len(counter)):
            if (max < counter[k]):
                max = counter[k]
        return max


