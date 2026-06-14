class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        profit = 0
        while j < len(prices):
            profit = max(profit, prices[j] - prices[i])
            if prices[j] >= prices[i]:
                j += 1
            else:
                i = j
        return profit
