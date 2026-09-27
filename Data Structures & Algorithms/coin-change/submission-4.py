class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            res = float("inf")
            for i in range(len(coins)):
                res = min(res, dfs(amount - coins[i]) + 1)
            memo[amount] = res
            return memo[amount]

        res = dfs(amount) 
        return -1 if res == float("inf") else res