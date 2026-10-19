class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## dfs(n) returns the minimum no of coins to make amount n
        hashMap = {}
        def dfs(amount):
            if amount in hashMap:
                return hashMap[amount]

            best = float("inf")
            for coin in coins:
                
                if coin == amount:
                    return 1
            
                
                if coin <= amount:
                    best = min(best, 1 + dfs(amount - coin))
            
            hashMap[amount] = best
            return hashMap[amount]

        if amount == 0:
            return 0

        res = dfs(amount)
        if res != float("inf"):
            return res
        else:
            return -1