class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        j = 1
        k = len(nums) - 1
        while i < len(nums) - 2:
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    while k - 1 >= 0 and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                elif total < 0:
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                else:
                    while k - 1 >= 0 and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
            j = i + 1
            k = len(nums) - 1
        return res
