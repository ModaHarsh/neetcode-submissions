class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## looks like a basical heap problem itself only
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        for c in range(0,k):
            res = heapq.heappop(heap)
        return -res     