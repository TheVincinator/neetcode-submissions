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
        def binarySearch(nums, target, l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1
        result = binarySearch(nums, target, 0, l - 1) 
        if result == -1:
            return binarySearch(nums, target, l, len(nums) - 1) 
        else:
            return result