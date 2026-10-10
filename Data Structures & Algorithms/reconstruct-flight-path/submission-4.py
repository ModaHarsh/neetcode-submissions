class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## okay so writing solution using hierholzer's algorithm
        ## textbook algorithm used to find eulerian path or a eulerian circuit
        ## for both directed and undirected graphs

        graph = {}
        for source, destination in tickets:
            graph.setdefault(source, []).append(destination)
            graph.setdefault(destination,[])

        for airport in graph:
            graph[airport].sort(reverse = True)

        stack = []
        res = []
        def dfs(airport):
            stack.append(airport)
            while stack:
                cur = stack[-1]
                if len(graph[cur]) == 0:
                    res.append(stack.pop())
                    continue
                
                stack.append(graph[cur].pop())
        
        dfs("JFK")
        return res[::-1]    