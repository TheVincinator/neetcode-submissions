class Solution:
    def numDecodings(self, s: str) -> int:
        chars = set()
        for i in range(1, 27):
            chars.add(str(i))

        memo = {}
        def dfs(i):
            if i >= len(s):
                return 1
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and s[i:i+2] in chars:
                res += dfs(i + 2)
            memo[i] = res
            return memo[i]

        return dfs(0)