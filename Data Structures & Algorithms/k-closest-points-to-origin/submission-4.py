class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairDistMap = defaultdict(list)
        distHeap = []
        for x, y in points:
            dist = math.sqrt((0 - x)**2 + (0 - y)**2)
            pairDistMap[dist].append([x, y])
            heapq.heappush(distHeap, dist)

        res = []
        for i in range(k):
            dist = heapq.heappop(distHeap)
            res.append(pairDistMap[dist].pop())

        return res