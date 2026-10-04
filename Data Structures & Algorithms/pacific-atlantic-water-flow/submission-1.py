class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## will try to solve using dfs approach
        ## code as required
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        
        def dfs(row, col):
            nonlocal flag1, flag2, mySet
            mySet.add((row, col))

            if (flag1 != 1) and (row == 0 or col == 0):
                flag1 = 1
            if (flag2 != 1) and (row == (len(heights)-1) or col == (len(heights[0])-1)):
                flag2 = 1
            
            if flag1 == 1 and flag2 == 1:
                return 1

            for dr, dc in directions:
                dR, dC = row + dr, col + dc

                if (0 <= dR < len(heights) and 0 <= dC < len(heights[0])
                and heights[dR][dC] <= heights[row][col] and 
                ((dR, dC) not in mySet)):
                    
                    if dfs(dR, dC) == 1:
                        return 1

                
        
        
        for i in range(len(heights)):
            for k in range(len(heights[0])):
                mySet = set()
                flag1, flag2 = 0, 0
                if dfs(i, k):
                    res.append([i,k])
        return res
                    




