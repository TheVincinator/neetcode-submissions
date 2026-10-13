class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []

        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1

        pairs = list(freqs.items())
        pairs.sort()

        for n, f in pairs:
            for _ in range(f):
                res.append(n)

        return res