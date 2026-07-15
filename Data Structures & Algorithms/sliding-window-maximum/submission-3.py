class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []

        i = 0
        j = 0
        while j < k:
            heapq.heappush(maxHeap, (-nums[j], j))
            j += 1

        res = []
        while j < len(nums):
            res.append(-maxHeap[0][0])
            i += 1
            while maxHeap and maxHeap[0][1] < i:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-nums[j], j))
            j += 1
        res.append(-maxHeap[0][0])

        return res

        