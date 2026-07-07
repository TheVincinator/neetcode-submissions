class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memo1 = [-1] * (len(nums) - 1)
        memo2 = [-1] * len(nums)
        def dp(i, length, memo):
            if i >= length:
                return 0
            if memo[i] >= 0:
                return memo[i]
            memo[i] = nums[i] + max(dp(i + 2, length, memo), dp(i + 3, length, memo))
            return memo[i]
        return max(dp(0, len(nums) - 1, memo1), dp(1, len(nums), memo2), dp(2, len(nums), memo2))