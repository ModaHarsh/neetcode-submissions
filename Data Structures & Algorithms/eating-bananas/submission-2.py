class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursForK(k):
            hrCount = 0
            for i in piles:
                hrCount += math.ceil(i / k)
            return hrCount
        
        maxPile = max(piles)

        r = maxPile         #faster than this does not make a difference
        l = 1               

        if h == len(piles):
            return max(piles)

        valid = 0
        while( l <= r ):
            
            mid = int((r + l)/2)

            if (h < hoursForK(mid)):      #koko too slow
                l = mid + 1

            elif(h >= hoursForK(mid)):      #valid answer need to narrow down
                valid = mid
                r = mid - 1

        return valid   