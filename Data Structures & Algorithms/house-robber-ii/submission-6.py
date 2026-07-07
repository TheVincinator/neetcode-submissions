class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.houseRobber(nums[1:]), self.houseRobber(nums[:-1]))

    def houseRobber(self, nums):
        memo = [-1] * len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] >= 0:
                return memo[i]
            memo[i] = nums[i] + max(dp(i + 2), dp(i + 3))
            return memo[i]
        return max(dp(0), dp(1))
