class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## at each step we can buy a coin
        ## we can sell a coin if we have one
        ## or we can skip it ??

        ## when buying we subtract coin value
        ## when selling we add coin value
        hashMap = {}

        def rec(i, canBuy):
            if i >= len(prices):
                return 0

            if (i, canBuy) in hashMap:
                return hashMap[(i, canBuy)]

            if canBuy:
                buy = rec(i + 1, False) - prices[i]
                skip = rec(i + 1, True)
                hashMap[(i, canBuy)] = max(buy, skip)
                return hashMap[(i, canBuy)]
            else:
                sell = rec(i + 2, True) + prices[i]
                hold = rec(i + 1, False)
                hashMap[(i, canBuy)] = max(sell, hold)
                return hashMap[(i, canBuy)]
            
        return rec(0, True)