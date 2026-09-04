class KthLargest:
    ## so this can be solved using heap basically then
    ## this can be solved using heap then
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:       ##smaller than k len heaps are still possibe
            heapq.heappop(self.heap) 

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            if len(self.heap) < self.k:
                return None
        else:
            if self.heap[0] < val:
                heapq.heapreplace(self.heap, val)
        return self.heap[0]




    ## intention is to heapify nums
    ## if len of nums more than k 
    ## create a heap of just the k largest elements
    ## and then replace if val > nums[0] or
    ## return nums[0]