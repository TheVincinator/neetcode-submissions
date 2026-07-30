class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for start, end, price in flights:
            adj_list[start].append((end, price))
        
        minHeap = []
        heapq.heappush(minHeap, (0, src, 0))
        best = defaultdict(lambda: float("inf"))
        res = -1
        while minHeap:
            price, start, kn = heapq.heappop(minHeap)
            if kn > k + 1:
                continue
            if start == dst:
                res = price
                return res
            best[(start, kn)] = price
            for end, flight_cost in adj_list[start]:
                new_cost = price + flight_cost
                if new_cost < best[(end, kn + 1)]:
                    best[(end, kn + 1)] = new_cost
                    heapq.heappush(minHeap, (new_cost, end, kn + 1))
        return res