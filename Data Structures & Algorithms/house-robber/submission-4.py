class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i - 2), dfs(i - 3)) + nums[i]
            return memo[i]

        return max(dfs(len(nums) - 1), dfs(len(nums) - 2))