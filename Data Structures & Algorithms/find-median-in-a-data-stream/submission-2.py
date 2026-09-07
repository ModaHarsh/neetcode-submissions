class MedianFinder:

    def __init__(self):
        self.median = None
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if self.median == None:
            self.median = num
            return
        
        if num > self.median:
            if (len(self.minHeap) - len(self.maxHeap)) == 1:
                heapq.heappush(self.maxHeap, -self.median)
                self.median = num
                while(self.median > self.minHeap[0]):
                    heapq.heappush(self.minHeap, self.median)
                    self.median = heapq.heappop(self.minHeap)
                return
            heapq.heappush(self.minHeap, num)

        elif num <= self.median:
            if (len(self.maxHeap) - len(self.minHeap)) == 1:
                heapq.heappush(self.minHeap, self.median)
                self.median = num
                while(self.median < -self.maxHeap[0]):
                    heapq.heappush(self.maxHeap, -self.median)
                    self.median = -heapq.heappop(self.maxHeap)
                return
            heapq.heappush(self.maxHeap, -num)

        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return self.median
        
        elif len(self.maxHeap) > len(self.minHeap):
            return (-self.maxHeap[0] + self.median) / 2
        
        elif len(self.minHeap) > len(self.maxHeap):
            return (self.minHeap[0] + self.median) / 2



        
        

        
        