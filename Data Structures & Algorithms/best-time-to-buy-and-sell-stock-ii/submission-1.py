class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[j - 1] > prices[j]:
                res += prices[j - 1] - prices[i]
                i = j
            j += 1
        res += prices[j - 1] - prices[i]
        return res