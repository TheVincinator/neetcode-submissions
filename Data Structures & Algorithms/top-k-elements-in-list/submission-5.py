class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        lst = sorted(list(freqs.items()), key = lambda x : -x[1])
        res = []
        for i in range(k):
            res.append(lst[i][0])
        return res
