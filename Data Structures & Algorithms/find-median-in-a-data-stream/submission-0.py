class MedianFinder:

    def __init__(self):
        self.minHeap = []
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        length = len(self.minHeap)
        popped = []
        if length % 2 == 1:
            # If length of min heap is odd
            mid = length // 2
            i = 0
            while i < mid:
                popped.append(heapq.heappop(self.minHeap))
                i += 1
            median = self.minHeap[0]
            for num in popped:
                heapq.heappush(self.minHeap, num)
            return median
        else:
            # If length of min heap is even
            mid1 = length // 2
            mid2 = mid1 - 1
            i = 0
            while i < mid2:
                popped.append(heapq.heappop(self.minHeap))
                i += 1
            median1 = heapq.heappop(self.minHeap)
            popped.append(median1)
            median2 = self.minHeap[0]
            for num in popped:
                heapq.heappush(self.minHeap, num)
            median = (median1 + median2) / 2
            return median
        