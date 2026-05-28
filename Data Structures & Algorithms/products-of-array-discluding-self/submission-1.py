class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefixArray[i] = prefix
            prefix *= nums[i]
        postfixArray = [1] * len(nums)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfixArray[i] = postfix
            postfix *= nums[i]
        result = []
        for i in range(len(nums)):
            result.append(prefixArray[i] * postfixArray[i])
        return result

        