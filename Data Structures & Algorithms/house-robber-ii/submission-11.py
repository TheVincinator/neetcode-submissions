class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        memo1 = {}
        memo2 = {}
        def dfs(i, nums, memo):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i + 2, nums, memo), dfs(i + 3, nums, memo)) + nums[i]
            return memo[i]
            
        return max(dfs(0, nums[:-1], memo1), dfs(1, nums, memo2), dfs(2, nums, memo2))