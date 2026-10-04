class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ## okay so for every 0 encountered
        ## compare level of bfs with value of cell
        ## if bfs level lesser than value
        ##      change value of the cell
        ## otherwise dont continue bfs in that route/return from
        ## there

        directions = [[0, 1], [1, 0], [0,-1], [-1,0]]

        
        def bfs(row, col):
            q = deque()
            q.append((row, col, 0))

            while q:
                cur = q.popleft()
                 
                for dr, dc in directions:
                    dRow, dCol = cur[0] + dr, cur[1] + dc
                    
                    if (dRow < 0 or dCol < 0
                    or dRow >= len(grid) or dCol >= len(grid[0]) or
                    grid[dRow][dCol] <= (cur[2] + 1)):
                        continue
                    
                    grid[dRow][dCol] = (cur[2] + 1)
                    q.append((dRow, dCol, cur[2] + 1))

                
                


        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 0:
                    bfs(i, k)
