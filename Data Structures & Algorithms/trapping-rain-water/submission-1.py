class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        prevMin = 0
        def waterInBetween(l, r):
            nonlocal prevMin
            max = ((r-l-1) * (min(height[l],height[r]) - prevMin))
            for i in range(l+1,r):
                if (height[i] >= min(height[l], height[r])):
                    max = max - (min(height[l], height[r]) - prevMin)
                elif (prevMin > height[i]):
                    max = max        #already been taken care of beforehand
                else: #In between level and prevMin
                    max = max - (height[i] - prevMin)
            prevMin = min(height[l], height[r])
            return max

        l, r = 0, (len(height) - 1)
        while((l<r) and (height[l] == 0)):
            l += 1
        while((l<r) and (height[r] == 0)):
            r -= 1
        while(l<r):
            water = water + waterInBetween(l,r)
            if (height[l] < height[r]):
                while (((l<r) and height[l] <= prevMin)):
                    l += 1
            elif (height[r] < height[l]):
                while (((l<r) and height[r] <= prevMin)):
                    r -= 1
            else:
                while((l<r) and (height[l] <= prevMin)):
                    l += 1
                while((l<r) and (height[r] <= prevMin)):
                    r -= 1
        return water

            



        

                
        