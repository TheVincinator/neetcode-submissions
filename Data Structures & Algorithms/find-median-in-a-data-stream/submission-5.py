class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.minHeap) + 1 < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        length = len(self.minHeap) + len(self.maxHeap)
        median = 0
        if length % 2 == 0:
            median = (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            median = self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
        return median