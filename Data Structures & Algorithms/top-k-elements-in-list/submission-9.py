class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key in freqs:
            buckets[freqs[key]].append(key)

        res = []
        i = len(nums)
        while k > 0:
            for n in buckets[i]:
                res.append(n)
                k -= 1
            i -= 1
        return res
