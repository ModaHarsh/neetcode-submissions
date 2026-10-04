class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## instead, trying to solve it by starting dfs
        ## from world borders

        ## flow water from world borders to whatever tile it can reach to
        ## insert it in set
        ## and then whichever tiles are present in both the sets return those

        directions = [[0, 1], [1,0], [0, -1], [-1,0]]
        pacific = set()
        atlantic = set()
        res = []

        def dfs(row, col, ocean):
            if (row, col) in ocean:
                return 
            ocean.add((row, col))
            
            for dr, dc in directions:
                dR, dC = row + dr, col + dc
                
                if (0 <= dR < len(heights) and 0 <= dC < len(heights[0])
                and ((dR, dC) not in ocean) and heights[dR][dC] >= heights[row][col]):
                    
                    dfs(dR, dC, ocean)

        for k in range(len(heights[0])):
            dfs(0, k, pacific)
        for i in range(len(heights)):
            dfs(i, 0, pacific)
        
        for k in range(len(heights[0])):
            dfs((len(heights)-1), k, atlantic)
        for i in range(len(heights)):
            dfs(i, (len(heights[0])-1), atlantic)

        for i in range(len(heights)):
            for k in range(len(heights[0])):
                if ((i, k) in pacific) and ((i, k) in atlantic):
                    res.append([i,k])
        return res
