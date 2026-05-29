class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maximum = 0
        for n in s:
            count = 1
            while (n + 1) in s:
                count += 1
                n += 1
            maximum = max(maximum, count)
        return maximum