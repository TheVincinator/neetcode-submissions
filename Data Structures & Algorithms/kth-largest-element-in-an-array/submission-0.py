class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        result = 0
        for _ in range(k):
            result = -heapq.heappop(maxHeap)
        return result