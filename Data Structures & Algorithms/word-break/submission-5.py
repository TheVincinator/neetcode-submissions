class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            res = False
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    res = dfs(i + len(word))
                    if res:
                        return res
            memo[i] = res
            return memo[i]

        return dfs(0)

            