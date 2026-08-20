class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # so first append pos and speed together in a tuple list
        # then calculate time to target in a separate array
        # then perform stack logic to find maximum no of fleet to arrive to the finish line


        posSpeed = []
        for i in range(len(position)):
            posSpeed.append((position[i], speed[i]))
        
        # sort by postion

        posSpeed.sort(key = lambda x: x[0])

        timeToTarget = []

        for i in range(len(position)):
            timeToTarget.append([((target - posSpeed[i][0])/posSpeed[i][1])])

        stack = []      #fleet count stack

        for i in range(len(timeToTarget)):
            if len(stack) == 0:
                stack.append(timeToTarget[i])
            
            else:

                    if(stack[-1][0] > timeToTarget[i][0]):
                        stack.append(timeToTarget[i])               #appending list
                    elif(stack[-1][0] == timeToTarget[i][0]):
                        stack[-1].append(timeToTarget[i][0])        #appending value toList
                
                    elif(stack[-1][0] < timeToTarget[i][0]):
                        while(len(stack)!= 0)and(timeToTarget[i][0] > stack[-1][0]):
                            timeToTarget[i].append(stack.pop())
                        stack.append(timeToTarget[i])
        
        return len(stack)
                

        


