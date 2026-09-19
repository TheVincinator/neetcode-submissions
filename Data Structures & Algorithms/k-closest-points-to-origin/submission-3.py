class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a dictionary that maps Euclidean distance to the corresponding pair
        # Calculate the Euclidean distance for each pair.
        # We add it to the dictionary
        # We add it to the heap
        # We do this for all pairs

        # We pop from the heap
        # We look for the corresponding Euclidean distance in the dictionary to find the corresponding pair
        # We add the pair to the result list
        # We do this k times
        # Return result list

        import math
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