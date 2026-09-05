class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ## can be solved with the help of a min heap
        ## and a separate function to solve/find the distance from origin
        def disOrigin(coord):
            x, y = coord[0], coord[1]
            return math.sqrt( (x)**2 + (y)**2 )
        
        heap = []
        for i in range(0, len(points)):
            heapq.heappush(heap, (disOrigin(points[i]), points[i])) 
        
        res = []
        
        for c in range(0,k):
            res.append(heapq.heappop(heap)[1])

        return res    