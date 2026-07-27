class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,2,3,3,4,4,5]
        if len(hand) % groupSize != 0:
            return False

        minHeap = []
        handMap = defaultdict(int)
        for card in hand:
            handMap[card] += 1
            if card not in minHeap:
                heapq.heappush(minHeap, card)

        start = minHeap[0]
        size = 0
        while handMap:
            if size == groupSize:
                start = minHeap[0]
                size = 0
            if start not in handMap:
                return False
            handMap[start] -= 1
            if not handMap[start]:
                if start != minHeap[0]:
                    return False
                heapq.heappop(minHeap)
                del handMap[start]
            size += 1
            start += 1
        return True
