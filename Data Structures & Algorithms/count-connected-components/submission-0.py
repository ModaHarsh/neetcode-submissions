class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## okay so only way which I can think of to do this will be by
        ## creating an overall visited node set and a count of the number
        ## of connected groups encountered so far that would work yes

        graph = [[] for _ in range(n)]
        processed = set()
        count = 0

        for node in edges:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])

        ## so no need to worry about cycle detection then
        ## remember visited only so we are not stuck forever in the cycle

        def dfs(node, visit):
            if node in visit:
                return
            processed.add(node)
            visit.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor, visit)

        

        for node in range(n):
            if node in processed:
                continue
            count += 1
            visit = set()
            dfs(node, visit)
        
        return count