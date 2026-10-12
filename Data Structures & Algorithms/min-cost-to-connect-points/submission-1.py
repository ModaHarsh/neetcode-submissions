class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ## okay so this can be solved using kruskal's algorithm
        ## we compute the manhattan distance between each pair of 
        ## points, and then we sort them in ascending order
        ## edges are chosen without forming cycles
        ## aka already connected/visited node edges are not chosen

        array = []
        
        for i in range(len(points)):
            for k in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[k][0]) + abs(points[i][1] - points[k][1])
                array.append((cost, (i, k)))

        array.sort()
        
        visit = []
        visit.append(set())
        totalCost = 0


        for edge in array:
            if (len(visit) == 1) and (len(visit[0]) == len(points)):
                break

            vertex1, vertex2 = edge[1][0], edge[1][1]
            cost = edge[0]
            
            flag1, flag2 = -1, -1
            
            for i in range(len(visit)):                
                if (vertex1 in visit[i]):
                    flag1 = i
                
                if (vertex2 in visit[i]):
                    flag2 = i
            
            if flag1 == flag2 and (flag1 != -1):    ## edges already joined case
                continue

            if (flag1 == -1) and (flag2 != -1):     ## joining an edge case
                visit[flag2].add(vertex1)
            
            if (flag1 != -1) and (flag2 == -1):
                visit[flag1].add(vertex2)

            if (flag1 == flag2) and (flag1 == -1):
                visit.append(set())
                visit[len(visit)-1].add(vertex1)
                visit[len(visit)-1].add(vertex2)

            if (flag1 != flag2) and (flag1 != -1) and (flag2 != -1):
                visit[flag1].update(visit[flag2])
                visit.pop(flag2)
            
            totalCost += cost 
        
        return totalCost







