class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for w in stones:
            heapq.heappush(heap, -w)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            res = max(x,y) - min(x,y)

            if res == 0:
                continue
            else:
                heapq.heappush(heap, -res)
        
        if len(heap) == 0:
            return 0
        else:
            return -heap[0]