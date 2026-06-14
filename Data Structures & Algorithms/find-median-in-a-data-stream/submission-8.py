class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.minHeap) + 1 < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2