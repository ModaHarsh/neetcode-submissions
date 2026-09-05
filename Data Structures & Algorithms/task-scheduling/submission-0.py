class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## so we can solve this problem with the help of a deque
        ## and a max heap to return the element with the max remaining frequency

        ## creating hashmap heap
        freqMap = {}
        for t in tasks:
            freqMap[t] = freqMap.setdefault(t, 0) + 1
        
        heap = []
        
        for key, value in freqMap.items():
            heapq.heappush(heap, [-value, key])

        que = deque()

        time = 0
        while heap or que:
            time += 1           # everysingle time a task from the heap needs to be processed
            
            if (que) and que[0][0] == time:
                heapq.heappush(heap, que.popleft()[1])

            if len(heap) == 0:
                continue


            task = heapq.heappop(heap)
            task[0] += 1
            
            if task[0] == 0:
                continue
            else: 
                que.append([time + n + 1, task])
        
        return time
            






 
        