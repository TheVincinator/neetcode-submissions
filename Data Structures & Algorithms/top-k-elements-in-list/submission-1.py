class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = defaultdict(int)
        for num in nums:
            numsMap[num] += 1
        pairs = list(numsMap.items())
        pairs.sort(key=lambda x: x[1])
        result = []
        i = len(pairs) - 1
        while k > 0:
            result.append(pairs[i][0])
            k -= 1
            i -= 1
        pairs.reverse()
        return result
