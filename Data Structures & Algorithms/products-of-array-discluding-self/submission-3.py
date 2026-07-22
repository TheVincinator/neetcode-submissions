class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefixArray[i] = prefix
            prefix *= nums[i]
        # [1, 1, 2, 8]
        postfixArray = [1] * len(nums)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfixArray[i] = postfix * prefixArray[i]
            postfix *= nums[i]
        return postfixArray
        # [48, 24, 6, 1]
