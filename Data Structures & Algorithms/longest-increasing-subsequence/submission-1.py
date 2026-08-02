class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            lengths = [1]
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lengths.append(1 + dp[j])
            dp[i] = max(lengths)

        return max(dp)