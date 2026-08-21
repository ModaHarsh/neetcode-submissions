class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findHeight(s, b):
            l = len(matrix[0])
            while(s<=b):
                height = int((s + b)/2)
                
                if(target > matrix[height][len(matrix[0])-1]):
                    s = height + 1
                elif(target < matrix[height][0]):
                    b = height - 1 
                else: 
                    return height
            return None

        height = findHeight(0, len(matrix)-1)
        if (height == None):
            return False
        
        l = 0
        r = len(matrix[0]) - 1
        while(l <= r):
            mid = int((l + r)/2)
            
            if(target > matrix[height][mid]):
                l = mid + 1
            elif(target < matrix[height][mid]):
                r = mid - 1
            else:
                return True
        return False



        