class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(lst, nums):
            result.append(lst.copy())
            for i in range(len(nums)):
                lst.append(nums[i])
                dfs(lst, nums[i + 1:])
                lst.pop()
        dfs([], nums)
        return result