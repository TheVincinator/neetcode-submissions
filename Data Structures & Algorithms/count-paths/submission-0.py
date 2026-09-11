class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = { (0, 0) : 1 }
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = dfs(r - 1, c) + dfs(r, c - 1)
            return memo[(r, c)]

        return dfs(m - 1, n - 1)