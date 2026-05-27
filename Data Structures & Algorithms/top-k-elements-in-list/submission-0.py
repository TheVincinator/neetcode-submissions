class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = defaultdict(int)
        for num in nums:
            numsMap[num] += 1
        pairs = list(numsMap.items())
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        result = []
        i = len(sorted_pairs) - 1
        while k > 0:
            result.append(sorted_pairs[i][0])
            k -= 1
            i -= 1
        result.reverse()
        return result
