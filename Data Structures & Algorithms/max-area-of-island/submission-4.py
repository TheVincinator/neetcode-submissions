class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            area = 1
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                area += dfs(r + dr, c + dc)
            return area

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))

        return res