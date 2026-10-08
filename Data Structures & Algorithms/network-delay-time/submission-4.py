class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        heap = [(0, k)]
        visit = set()
        last_arrival = 0

        while heap:
            arrival_time, node = heapq.heappop(heap)

            if node in visit:
                continue
            
            visit.add(node)
            last_arrival = arrival_time

            for neighbor, travel_time in graph[node]:
                if neighbor not in visit:
                    heapq.heappush(heap, (arrival_time + travel_time, neighbor))
        
        return last_arrival if len(visit) == n else -1