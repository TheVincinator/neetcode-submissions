class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,2,3,3,4,4,5]
        if len(hand) % groupSize != 0:
            return False

        handMap = defaultdict(int)
        for card in hand:
            handMap[card] += 1

        start = min(handMap)
        size = 0
        while handMap:
            if size == groupSize:
                start = min(handMap)
                size = 0
            if start not in handMap:
                return False
            handMap[start] -= 1
            if not handMap[start]:
                del handMap[start]
            size += 1
            start += 1
        return True
