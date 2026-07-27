class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,2,3,3,4,4,5]
        if len(hand) % groupSize:
            return False

        handMap = defaultdict(int)
        for card in hand:
            handMap[card] += 1
        minHeap = list(handMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(groupSize):
                curr = start + i
                if curr not in handMap:
                    return False
                handMap[curr] -= 1
                if not handMap[curr]:
                    if curr != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
                    del handMap[curr]
        return True
