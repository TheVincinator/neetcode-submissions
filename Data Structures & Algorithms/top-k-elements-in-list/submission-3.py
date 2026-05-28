class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
