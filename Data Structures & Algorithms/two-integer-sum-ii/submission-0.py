class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have two pointers left and right
        # and use logic if l + r < target increment l
        #           and if l + r > target decremetn r
        arr = []
        l,r = 0, len(numbers)-1
        while(l<r):
            if (numbers[l] + numbers[r] > target):
                r -= 1
            elif (numbers[l] + numbers[r] < target):
                l += 1
            else:
                arr.append(l+1)
                arr.append(r+1)
                return arr
    
        