class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        hashMap = {}
        for i in range(len(hand)):
            hashMap[hand[i]] = hashMap.setdefault(hand[i], 0) + 1
        
        hand.sort()
        
        for i in range(len(hand)):
            if hashMap[hand[i]] != 0:
                for k in range(groupSize):
                    if (hand[i] + k) not in hashMap:
                        return False
                    hashMap[hand[i] + k] -= 1
                    if hashMap[hand[i] + k] < 0:
                        return False

        return True