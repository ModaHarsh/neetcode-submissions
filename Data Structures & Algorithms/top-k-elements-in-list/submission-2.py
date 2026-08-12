class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for i in range(0, len(nums)):
            if nums[i] not in groups:
                groups[nums[i]] = 0
            groups[nums[i]] += 1           # key:value pair getting incremented

        freq = [[] for i in range(len(nums) + 1 )]       
        for key, values in groups.items():
            freq[values].append(key)     #appending nums to index which denotes freq

        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        