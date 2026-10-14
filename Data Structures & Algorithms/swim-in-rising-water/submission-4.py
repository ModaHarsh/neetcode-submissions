class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        visit.add((0, 0))
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], 0, 0))

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while minHeap:
            t, row, col = heapq.heappop(minHeap)
            
            if row == N - 1 and col == N - 1:
                return t
            
            
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if newRow < 0 or newCol < 0 or newRow >= N or newCol >= N or (newRow, newCol) in visit:
                    continue
                visit.add((newRow, newCol))
                heapq.heappush(minHeap, (max(t, grid[newRow][newCol]), newRow, newCol))

            