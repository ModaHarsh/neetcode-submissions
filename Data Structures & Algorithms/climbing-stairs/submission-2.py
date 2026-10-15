class Solution:
    def climbStairs(self, n: int) -> int:
        ## top - down 
        cache = {}
        def rec(n):
            nonlocal cache
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]
            
            cache[n] = rec(n - 1) + rec(n - 2)
            return cache[n]
        
        return rec(n)