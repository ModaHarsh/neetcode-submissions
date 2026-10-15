class Solution:
    def climbStairs(self, n: int) -> int:
        ## okay so we basically have to return the number of leaf nodes 
        
        ## bottom up

        array = [1,1]

        for i in range(n-1):
            tmp = array[1]
            array[1] = array[0] + array[1]
            array[0] = tmp

        return array[1]