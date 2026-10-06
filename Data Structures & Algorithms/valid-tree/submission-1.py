class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## forming a valid adjacency list for now
        
        graph = [[] for _ in range(n)]
        visit = set()
        arr = []

        for node in edges:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])
        
        def dfs(node, visit, parent):
            if node in visit:
                return False

            arr.append(node)
            visit.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, visit, node):
                    visit.remove(node)
                    return False
            
            visit.remove(node)
            return True

        parent = None

        if not dfs(0, visit, None):
            return False
        
        if len(arr) == n:
            return True
        else:
            return False