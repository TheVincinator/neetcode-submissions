class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maximum = 0
        for n in s:
            if (n-1) not in s:
                length = 1
                nxt = n + 1
                while nxt in s:
                    length += 1
                    nxt += 1
                maximum = max(maximum, length)
        return maximum