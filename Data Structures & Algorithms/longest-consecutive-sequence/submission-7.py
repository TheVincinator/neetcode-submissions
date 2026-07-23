class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for n in numsSet:
            length = 0
            if (n - 1) not in numsSet:
                while n in numsSet:
                    n += 1
                    length += 1
                res = max(res, length)
        return res