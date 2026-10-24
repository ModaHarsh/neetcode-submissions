class Solution:
    def jump(self, nums: List[int]) -> int:
        ## can be solved using recursion
        ## let rec(i) return the min number of steps needed
        ## to get to the index (n - 1)
        arr = [float("inf")] * len(nums)

        def rec(i):
            if i >= len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float("inf")

            if arr[i] != float("inf"):
                return arr[i]

            count = float("inf")
            
            for jumpLength in range(1, nums[i] + 1):
                count = min(1 + rec(i + jumpLength), count)
            
            arr[i] = count
            return arr[i]
            

        return rec(0)  