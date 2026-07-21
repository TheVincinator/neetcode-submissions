class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        i = 1
        res = curSum
        while i < len(nums):
            res = max(res, curSum)
            if curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            i += 1
        res = max(res, curSum)
        return res