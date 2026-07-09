class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i, j = 0, 1
        prev = prices[0]
        while j < len(prices):
            if prev > prices[j]:
                res += prices[j - 1] - prices[i]
                prev = prices[j]
                i = j
            else:
                prev = prices[j]
                j += 1
        res += prices[j - 1] - prices[i]
        return res