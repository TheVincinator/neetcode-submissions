class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMap = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        result = []
        def dfs(curr, dig):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return
            for d in dig:
                for c in digitsMap[d]:
                    curr.append(c)
                    dfs(curr, dig[1:])
                    curr.pop()
                break
        if digits:
            dfs([], digits)
        return result
