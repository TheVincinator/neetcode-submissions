class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(openN, closedN, curr):
            if openN == closedN == n:
                result.append(curr)
                return
            if openN < n:
                dfs(openN + 1, closedN, curr + "(")
            if closedN < openN:
                dfs(openN, closedN + 1, curr + ")")
        dfs(0, 0, "")
        return result
