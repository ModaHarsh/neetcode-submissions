class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = {}
        for flight in flights:
            graph.setdefault(flight[0],[]).append( (flight[2], flight[1]) )
            graph.setdefault(flight[1],[])


        visit = set()
        res = float("inf")
        hashMap = {}
        
        def bfs(node):
            nonlocal res
            q = deque()

            visit.add(node)
            q.append((node, 0, 0)) ## node, price, level
            while q:
                node, price, level = q.popleft()
                hashMap[node] = price
                if level > k + 1:
                    continue
                
                if node == dst:
                    res = min(res, price)
                
                for neighbor in graph[node]:
                    if neighbor[1] in visit:
                        continue
                    if hashMap.get(neighbor[1], float("inf")) < (price + neighbor[0]):
                        continue

                    q.append((neighbor[1], price + neighbor[0], level + 1))
        
        bfs(src)
        if res != float("inf"): 
            return res 
        else: 
            return -1
        
