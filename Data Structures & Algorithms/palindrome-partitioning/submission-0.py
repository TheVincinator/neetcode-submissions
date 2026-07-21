class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def dfs(lst, i):
            if i >= len(s):
                result.append(lst.copy())
                return
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    lst.append(s[i:j+1])
                    dfs(lst, j + 1)
                    lst.pop()
        dfs([], 0)
        return result

            