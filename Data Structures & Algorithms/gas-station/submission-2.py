class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        effect = []
        totalEffect = 0
        for i in range(len(gas)):
            effect.append(int(gas[i] - cost[i]))
            totalEffect += effect[i]
        ## effect[i] represents the overall effect of arriving/
        ## starting from the station i on the tank of the vehicle

        ## running sum should never be negative or we need to 
        ## start again 

        if totalEffect < 0:
            return -1

        runningEffect = 0
        res = 0
        for i in range(len(effect)):
            runningEffect += effect[i]
            
            if runningEffect < 0:
                
                if i == len(effect):
                    return -1

                res = i + 1
                runningEffect = 0
                continue
        
        return res