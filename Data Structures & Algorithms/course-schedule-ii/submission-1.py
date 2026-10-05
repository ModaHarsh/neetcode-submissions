class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visit = set()
        safe = set()
        res = []

        def dfs(node, visit):
            if node in visit:
                return False
            if node in safe:
                return True
            
            visit.add(node)

            for pre in graph[node]:
                if not dfs(pre, visit):
                    visit.remove(node)
                    return False
            
            visit.remove(node)
            safe.add(node)
            res.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node, visit):
                return []
        return res
