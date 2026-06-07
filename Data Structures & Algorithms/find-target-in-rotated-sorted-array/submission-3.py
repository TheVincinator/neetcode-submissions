class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        def binarySearch(nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1
        result = binarySearch(nums[l:], target) if target in nums[l:] else binarySearch(nums[:l], target)
        if result == -1:
            return -1
        else:
            return result + l if target in nums[l:] else result