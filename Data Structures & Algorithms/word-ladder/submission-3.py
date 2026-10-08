class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ## okay so first forming the graph in the form of dictionary
        if endWord not in wordList:
            return 0

        graph = {}
        for word in wordList:
            graph[word] = []
        
        graph.setdefault(beginWord, [])

        ## okay so now our graph has been formed and we just need to form 
        ## edges for the graph

        ## wildcard matches
        wildDict = {}
        def wildcard(word):
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                wildDict.setdefault(key, []).append(word)
        
        for word in graph.keys():
            wildcard(word)
        
        for bucket in wildDict.values():
            for i in range(len(bucket)):
                for j in range(i + 1, len(bucket)):
                    graph[bucket[i]].append(bucket[j])
                    graph[bucket[j]].append(bucket[i])

        # graph finally formed now

        def bfs(beginWord):
            q = deque()
            
            count = 1
            parent = None
            visit = set()
            q.append((beginWord, count))

            while q:
                curWord, curCount = q.popleft()
                if curWord in visit:
                    continue
                visit.add(curWord)
                
                for neighbor in graph[curWord]:
                    
                    if (neighbor in visit):
                        continue
                    
                    if neighbor == endWord:
                        return curCount + 1                    
                    
                    q.append((neighbor, curCount + 1))

        if bfs(beginWord) != None:
            return bfs(beginWord)
        else:
            return 0