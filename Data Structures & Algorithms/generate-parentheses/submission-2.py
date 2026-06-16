class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(o, c, curr):
            if o == c == n:
                result.append(curr)
                return
            if len(curr) == n * 2:
                return
            if o > c:
                dfs(o + 1, c, curr + "(")
                dfs(o, c + 1, curr + ")")
            else:
                dfs(o + 1, c, curr + "(")
        dfs(0, 0, "")
        return result
