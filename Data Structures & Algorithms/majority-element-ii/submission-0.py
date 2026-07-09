class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        res = []
        for key in freqMap:
            if freqMap[key] > len(nums) / 3:
                res.append(key)
        return res