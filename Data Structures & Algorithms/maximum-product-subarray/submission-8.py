class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum, maximum = 1, 1
        res = float("-inf")
        for n in nums:
            minimum, maximum = min(minimum * n, maximum * n, n), max(minimum * n, maximum * n, n)
            res = max(res, maximum)
        return res