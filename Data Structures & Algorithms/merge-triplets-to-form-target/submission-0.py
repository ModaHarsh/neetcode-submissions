class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ## okay so for whatever
        ## triplets our target values reside in 
        ## for those set of triplets our
        ## target values should be the maximum in those columns

        ## okay so we can solve the problem in three scans
        
        ## first column
        flag1, flag2, flag3 = 0, 0, 0
        
        for triplet in triplets:
            if triplet[0] == target[0]:
                if triplet[1] <= target[1] and triplet[2] <= target[2]:
                    flag1 = 1
            
            if triplet[1] == target[1]:
                if triplet[0] <= target[0] and triplet[2] <= target[2]:
                    flag2 = 1

            if triplet[2] == target[2]:
                if triplet[0] <= target[0] and triplet[1] <= target[1]:
                    flag3 = 1
        
        if flag1 and flag2 and flag3:
            return True
        else:
            return False