class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maximum = 0
        count = 1
        for n in s:
            nxt = n + 1
            while nxt in s:
                count += 1
                nxt += 1
            maximum = max(maximum, count)
            count = 1
        return maximum