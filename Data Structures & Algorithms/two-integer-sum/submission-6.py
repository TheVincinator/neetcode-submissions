class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                diff = target - nums[i]
                d[diff] = i
            else:
                return [d[nums[i]], i]