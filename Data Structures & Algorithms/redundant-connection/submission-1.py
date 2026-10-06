class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        ## trying a different more efficient apporach apparently
        ## to solve by first completely forming the graph
        ## and then finding the cycle elements
        ## and then finding the last edge added connecting any 
        ## of the two cyclic elements

        ## cycle start is found when a visited node is found again

        graph = [[] for _ in range(len(edges))]
        visit = []
        cycleStart = None
        t = None
        cycle = set()
        
        for node in edges:
            graph[node[0] - 1].append(node[1] - 1)
            graph[node[1] - 1].append(node[0] - 1)

        def dfs(node, visit, parent):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return False

            
            visit.append(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, visit, node):
                    return False

            
            visit.remove(node)
            return True
        
        
        dfs(1, visit, -1)
        for i in range(len(visit)):
            if visit[i] == cycleStart:
                t = i
            if (t != None) and  i >= t:
                cycle.add(visit[i])
        
        for edge in edges[::-1]:
            if ((edge[0] - 1) in cycle) and ((edge[1] - 1) in cycle):
                return edge