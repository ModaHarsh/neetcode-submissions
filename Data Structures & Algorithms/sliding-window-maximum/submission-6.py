import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        heap = []  # stores (-value, index)
        l = 0

        # build initial max heap for first window and append its max
        for r in range(0, k):
            heapq.heappush(heap, (-nums[r], r))

        arr.append(-heap[0][0])

        # slide the window
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            l = r - k + 1

            # discard stale entries (indices that fell out of the window)
            while heap[0][1] < l:
                heapq.heappop(heap)

            arr.append(-heap[0][0])

        return arr 