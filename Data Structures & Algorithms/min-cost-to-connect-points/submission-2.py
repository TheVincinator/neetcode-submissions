class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        heapq.heappush(minHeap, [0, 0])
        visited = set()
        res = 0
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += dist
            visited.add(node)
            for i in range(len(points)):
                if i in visited:
                    continue
                x1, y1 = points[node][0], points[node][1]
                x2, y2 = points[i][0], points[i][1]
                manhattanDist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, [manhattanDist, i])
        return res