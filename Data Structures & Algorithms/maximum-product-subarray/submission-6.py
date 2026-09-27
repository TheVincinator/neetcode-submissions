class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum = 1
        maximum = 1
        res = float("-inf")
        for n in nums:
            minimum, maximum = min(minimum * n, maximum * n, n), max(minimum * n, maximum * n, n)
            res = max(res, maximum)
            if minimum == 0:
                minimum = 1
            if maximum == 0:
                maximum = 1
        return res