class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        hashMap = {}

        def rec(i, amount):
            if amount == 0:
                return 1
            
            if i >= len(coins):
                return 0

            if (i, amount) in hashMap:
                return hashMap[(i, amount)]



            if coins[i] <= amount:
                take = rec(i, amount - coins[i])
                leave = rec(i + 1, amount)
                
                hashMap[(i, amount)] = take + leave
                return hashMap[(i, amount)]
            
            hashMap[(i, amount)] = rec(i + 1, amount)
            return hashMap[(i, amount)]
        
        return rec(0, amount)