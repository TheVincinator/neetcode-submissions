class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            maximum = l
            for i in range(l, r + 1):
                maximum = max(maximum, i + nums[i])
            l = r + 1
            r = maximum
            res += 1
        return res