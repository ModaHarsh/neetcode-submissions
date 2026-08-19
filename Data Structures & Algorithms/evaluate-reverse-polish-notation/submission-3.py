class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a,b):
            return int(a + b)
        def sub(a,b):
            return int(a - b)
        def multi(a,b):
            return int(a * b)
        def divide(a,b):
            return int(a / b)

        operator = {'+': add, '-': sub, '*': multi, '/': divide}
        
        stack = []

        for t in tokens:
            if t not in operator:
                stack.append(int(t))
            if t in operator:
                b = stack.pop()
                a = stack.pop()
                stack.append(operator[t](a,b))
        
        return stack.pop()





                


        
        