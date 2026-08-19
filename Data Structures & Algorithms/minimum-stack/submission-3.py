class MinStack:

    def __init__(self):
        self.minStack = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.min.append(val)

        if val <= self.min[-1]:
            self.min.append(val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        if self.minStack[-1] == self.min[-1]:
            if (len(self.minStack) == 0):
                self.min = []
            elif (len(self.minStack) == 1):
                self.min = []
            else: 
                self.min.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
