class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ## trying to solve with multi source bfs approach

        directions = [[0, 1], [1, 0], [0,-1], [-1,0]]
        q = deque()


        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 0:
                    q.append((i, k, 0))
        
        while q:
            curr = q.popleft()
            for dr, dc in directions:
                dR, dC = curr[0] + dr, curr[1] + dc

                if (( 0 <= dR < len(grid) ) and (0 <= dC < len(grid[0])
                and grid[dR][dC] > (curr[2] + 1))):
                    grid[dR][dC] = curr[2] + 1
                    q.append((dR, dC, curr[2] + 1))

            
