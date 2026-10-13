class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1

        res = []
        pairs = list(freqs.items())
        pairs.sort(key = lambda x : x[1])
        for _ in range(k):
            key, _ = pairs.pop()
            res.append(key)

        return res