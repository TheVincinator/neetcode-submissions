class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(total):
            if total == amount:
                return 0
            if total > amount:
                return float("inf")
            if total in memo:
                return memo[total]

            ans = float("inf")

            for coin in coins:
                ans = min(ans, 1 + dfs(total + coin))

            memo[total] = ans
            return ans

        res = dfs(0)
        return res if res != float("inf") else -1