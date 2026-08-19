class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oBrackets = ('(', '{', '[')
        cBrackets = (')', '}', ']')

        for i in range(len(s)):
            if s[i] in oBrackets:
                stack.append(s[i])
            if s[i] in cBrackets:
                if s[i] == ')':
                    if len(stack)!= 0 and stack[-1] == '(':
                        stack.pop()
                    else: 
                        return False

                if s[i] == '}':
                    if len(stack)!= 0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                    
                if s[i] == ']':
                    if len(stack)!= 0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False



        