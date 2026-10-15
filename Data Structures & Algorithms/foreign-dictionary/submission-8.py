class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ## comparison between two consecutive words
        ## gives us a directed edge
        ## then run topological sort

        graph = {}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            flag = 0
            for ci in range(min(len(w1), len(w2))):
                if w1[ci] == w2[ci]:
                    continue
                flag = 1
                graph.setdefault(w2[ci], []).append(w1[ci])
                graph.setdefault(w1[ci], [])
                break
            
            if flag == 0 and len(w1) > len(w2):
                return ""

            



        ## graph formed..every node points towards a smaller node then
        res = []
        path = set()
        visit = set()
    
        def dfs(node, visit, path):
            if node in path:
                return False
            
            if node in visit:
                return True
        
            visit.add(node)
            path.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor, visit, path):
                    return False
            
            res.append(node)
            path.remove(node)
            return True

        

        for character in graph.keys():
            if not dfs(character, visit, path):
                return ""
        
        for word in words:
            for c in word:
                if len(res) == 26:
                    break
                if (c not in visit):
                    visit.add(c)
                    res.append(c)
        
        return ''.join(res)
