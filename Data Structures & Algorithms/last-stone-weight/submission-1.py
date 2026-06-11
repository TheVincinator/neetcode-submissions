class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) >= 2:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x == y:
                continue
            updatedStone = min(x, y) - max(x, y)
            heapq.heappush(maxHeap, updatedStone)
        return 0 if not maxHeap else -maxHeap[0]