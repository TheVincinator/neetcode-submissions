class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = defaultdict(int)
        for t in tasks:
            freqMap[t] += 1
        maxHeap = [-count for count in freqMap.values()]
        heapq.heapify(maxHeap)
        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
