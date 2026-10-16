class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## trying bottom - up approach here now   
        cost = cost + [0]
        array = [0] * len(cost)
        i = 0
        
        while(i <= len(cost) - 1):
            if i <= 1:
                array[i] = cost[i]
                i += 1
                continue
            
            array[i] = cost[i] + min(array[i-1], array[i - 2])
            i += 1

        return array[len(cost) - 1]