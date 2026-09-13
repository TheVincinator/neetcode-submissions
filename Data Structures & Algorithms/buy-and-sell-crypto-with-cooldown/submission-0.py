class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy = True
        # Sell = False
        memo = {}
        def dfs(i, action):
            if i >= len(prices):
                return 0
            if (i, action) in memo:
                return memo[(i, action)]
            if action:
                memo[(i, action)] = max(dfs(i + 1, False) - prices[i], dfs(i + 1, action))
            else:
                memo[(i, action)] = max(dfs(i + 2, True) + prices[i], dfs(i + 1, action))
            return memo[(i, action)]

        return dfs(0, True)