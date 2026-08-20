class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # so you basically need two arrays
        # a1 = index of first bar to the left of ith bar which is smaller than i
        # a2 = index of first bar to the right of ith bar which is smaller than i
        
        
        lBound = [0] * len(heights)
        rBound = [0] * len(heights)
        stack = []
        for i in range(0, len(heights)):
            if len(stack) == 0:
                stack.append((heights[i],i))
            else:
                if heights[i] >= stack[-1][0]:
                    stack.append((heights[i],i))
                else:
                    while (len(stack) != 0) and (heights[i] < stack[-1][0]):
                        rBound[stack[-1][1]] = i            #smaller at index pointed
                        stack.pop()
                    stack.append((heights[i],i))
        for s in stack:
            rBound[s[1]] = len(heights)
        
        stack = []
        for i in range(len(heights)-1, -1, -1):
            if len(stack) == 0:
                stack.append((heights[i],i))
            else:
                if heights[i] >= stack[-1][0]:
                    stack.append((heights[i],i))
                else:
                    while (len(stack) != 0) and (heights[i] < stack[-1][0]):
                        lBound[stack[-1][1]] = i                 #smaller at index pointed
                        stack.pop()
                    stack.append((heights[i],i))
        for s in stack: 
            lBound[s[1]] = -1

        def maxForBar(i):
            l = lBound[i]
            r = rBound[i]
            return heights[i] * (r - l - 1)


        res = 0
        for i in range(len(heights)):
            if res < maxForBar(i):
                res = maxForBar(i)
        
        return res