class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyPairs = {};
        for n in range(0, len(nums)):
            if (nums[n] not in frequencyPairs):
                frequencyPairs[nums[n]] = 0
            frequencyPairs[nums[n]] += 1

        sortedData = dict(sorted(frequencyPairs.items(), key=lambda item: item[1], reverse = True))
        return list(sortedData.keys())[0:k]

        
        