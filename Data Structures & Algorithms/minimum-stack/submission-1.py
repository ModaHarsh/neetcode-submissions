class MinStack:

    def __init__(self):
        self.minStack = []
        self.min = None

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.min = val

        if val < self.min:
            self.min = val
        self.minStack.append(val)
        
        

    def pop(self) -> None:
        if self.minStack[-1] == self.min:
            if (len(self.minStack) <= 1):
                self.min = None
            else: 
                self.min = self.minStack[0]
                for n in range(len(self.minStack)-1):
                    if self.minStack[n] < self.min:
                        self.min = self.minStack[n]
        self.minStack.pop()



    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.min
            

        
