class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, maximum):
            if (i, maximum) in memo:
                return memo[(i, maximum)]
            if i >= len(nums):
                return 0
            if nums[i] > maximum:
                memo[(i, maximum)] = max(dfs(i + 1, nums[i]) + 1, dfs(i + 1, maximum))
            else:
                memo[(i, maximum)] = dfs(i + 1, maximum)
            return memo[(i, maximum)]

        return dfs(0, float("-inf"))