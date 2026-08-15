class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(0, len(prices)-1):
            for j in range(i + 1, len(prices)):
                if (prices[j] - prices[i]) > max:
                    max = prices[j] - prices[i]
        return max
        