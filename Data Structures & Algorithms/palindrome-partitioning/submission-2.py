class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(lst, i):
            if i >= len(s):
                res.append(lst.copy())
                return
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    lst.append(s[i:j+1])
                    dfs(lst, j + 1)
                    lst.pop()
        dfs([], 0)
        return res

    def isPalin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


            