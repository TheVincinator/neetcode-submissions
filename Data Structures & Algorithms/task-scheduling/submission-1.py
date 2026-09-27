class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = defaultdict(int)
        for task in tasks:
            freqs[task] += 1

        maxHeap = []
        for task in freqs:
            heapq.heappush(maxHeap, -freqs[task])

        queue = deque()
        time = 0
        while maxHeap or queue:
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq + 1 != 0:
                    queue.append((freq + 1, time + n))
            while queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
            time += 1

        return time