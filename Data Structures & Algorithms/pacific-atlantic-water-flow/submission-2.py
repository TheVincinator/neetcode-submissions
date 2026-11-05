class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        atlantic = set()
        pacific = set()
        def dfs(r, c, s):
            s.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                r_n = r + dr
                c_n = c + dc
                if r_n >= 0 and r_n < ROWS and c_n >= 0 and c_n < COLS and (r_n, c_n) not in s and heights[r_n][c_n] >= heights[r][c]:
                    dfs(r_n, c_n, s)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    dfs(r, c, pacific)
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    dfs(r, c, atlantic)

        res = []
        for (r, c) in atlantic:
            if (r, c) in pacific:
                res.append([r, c])
        
        return res