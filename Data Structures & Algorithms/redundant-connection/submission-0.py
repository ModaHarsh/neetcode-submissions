class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ## check if the graph is cyclic at the addition of each
        ## edge if it turns cyclic at the addition of an edge then
        ## we can just return that edge

        graph = [[] for _ in range(len(edges))]

        def dfs(node, visit, parent):
            
            if node in visit:
                return False

            visit.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, visit, node):
                    visit.remove(node)
                    return False
            
            visit.remove(node)
            return True
        
        for node in edges:
            graph[node[0] - 1].append(node[1] - 1)
            graph[node[1] - 1].append(node[0] - 1)
            visit = set()
            if not dfs(node[0] - 1, visit, None):
                return node        