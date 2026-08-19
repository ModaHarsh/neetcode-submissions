class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # okay understood using hint4
        stack = []
        arr = [0] * len(temperatures)
        

        for t in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[t], t))
            if len(stack) != 0:   
                if temperatures[t] <= stack[-1][0]:
                    stack.append((temperatures[t], t))
            
                else:
                    while (len(stack) != 0) and(temperatures[t] > stack[-1][0]):
                        popped = stack.pop()
                        arr[popped[1]] = (t - popped[1])
                    stack.append((temperatures[t], t))

                
        for s in stack:
            arr[s[1]] = 0
        
        return arr

                
        