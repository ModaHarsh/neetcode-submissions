class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## solving by putting in into graph logic and understanding 

        graph = [[] for _ in range(numCourses)]
        safe = set()

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        def dfs(node, visit):
            if node in visit:
                return False
            if node in safe:
                return True
                
            visit.add(node)
            
            for pre in graph[node]:
                if not dfs(pre, visit):
                    return False
            visit.remove(node)
            safe.add(node)
            return True

        visit = set()
        for node in range(numCourses):
            if not dfs(node, visit):
                return False
        return True
        
        ## just hitting TLE with my approach here