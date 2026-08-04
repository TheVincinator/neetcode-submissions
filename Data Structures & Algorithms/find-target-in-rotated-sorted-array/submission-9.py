class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                if target < nums[mid] and target <= nums[r]:
                    l = mid + 1
                elif target < nums[mid] and target > nums[r]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    return mid
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                elif target > nums[mid] and target > nums[r]:
                    r = mid - 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    return mid

        return -1