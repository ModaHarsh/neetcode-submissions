class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## okay so this is basically a bfs approach problem
        ## along with check at last if all fruits are
        ## rotten or not at last simple linear scan
        ## I would say

        ## multisource bfs where max level reached is the minutes
        ## required
        q = deque()
        res = 0
        directions = [[0, 1], [0, -1], [1,0], [-1,0]]
        
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 2:
                    q.append((i, k, 0))

        while q:
            cur = q.popleft()
            
            res = max(res, cur[2])
            
            for dr, dc in directions:
                dR, dC = cur[0] + dr, cur[1] + dc
                
                if (0 <= dR < len(grid) and 0 <= dC < len(grid[0])
                and grid[dR][dC] == 1):
                
                    grid[dR][dC] = 2
                    q.append((dR, dC, cur[2] + 1))
        
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 1:
                    return -1
        return res
            

            
