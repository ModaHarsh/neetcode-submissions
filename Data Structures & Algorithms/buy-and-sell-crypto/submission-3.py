class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to solve using two pointers apporach aswell
        # to get O(n) complexity
        l,r = 0,1
        max = 0
        while((l<r) and (r < (len(prices)))):
            if(prices[l] > prices[r]):
                l = r
                if (r != len(prices)-1):
                    r += 1
            if ((prices[r] - prices[l]) > max):
                max = (prices[r] - prices[l])
            r += 1
        return max