class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for s, e, t, in times:
            adj_list[s].append([t, e])

        minHeap = []
        heapq.heappush(minHeap, [0, k])
        visited = set()
        res = 0
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res = t
            visited.add(node)
            for time, neighbor in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [t + time, neighbor])
        
        if len(visited) == n:
            return res
        else:
            return -1


        