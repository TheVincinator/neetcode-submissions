class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distance = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
            heapq.heappush(distances, (distance, [x, y]))
        result = []
        for _ in range(k):
            d, lst = heapq.heappop(distances)
            result.append(lst)
        return result