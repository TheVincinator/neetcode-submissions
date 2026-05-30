class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maximum = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                maximum = max(maximum, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return maximum
