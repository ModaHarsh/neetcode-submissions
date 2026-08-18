class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        heap = []
        l = 0        

        # build initial max heap for first window and
        # append its max to arr
        for r in range(0,k):
            heapq.heappush(heap, (-nums[r], r))
        
        arr.append(-heap[0][0])

        
        # for every increasing r(window shifting) remove nums[l]
        # from the max heap and then add nums[r] in the max heap
        # and then get the max element in O(1) and then append that 
        # to arr
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            l += 1

            while heap[0][1] < l:   # checking if max element is still
               heapq.heappop(heap)  # in the window if not removing from heap
            
            arr.append(-heap[0][0])
        return arr



        