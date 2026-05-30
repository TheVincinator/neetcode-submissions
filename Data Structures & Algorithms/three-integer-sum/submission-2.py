class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            k = len(nums) - 1
            l = i + 1
            while l < k:
                j = l
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        if [nums[i], nums[j], nums[k]] not in result:
                            result.append([nums[i], nums[j], nums[k]])
                        break
                l += 1
        return result