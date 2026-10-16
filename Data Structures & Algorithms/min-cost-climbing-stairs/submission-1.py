class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        hashMap = {}
        def rec(n):
            if n in hashMap:
                return hashMap[n]
            if n <= 1:
                return cost[n]

            hashMap[n] = cost[n] + min(rec(n-1), rec(n-2))
            return hashMap[n]
        
        return rec(len(cost) - 1)
