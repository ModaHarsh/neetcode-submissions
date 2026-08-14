class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = set(numbers)
        arr = []
        for i in range(0, len(numbers)):
            if (target-numbers[i]) in numSet:
                for j in range(0, len(numbers)):
                    if i == j:
                        continue
                    if numbers[j] == (target-numbers[i]):
                        arr.append(i + 1)
                        arr.append(j + 1)
                        return arr
            