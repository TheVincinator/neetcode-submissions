class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (r < 0
                or r >= rows
                or c < 0 
                or c >= cols
                or (r, c) in visited 
                or grid[r][c] == 0):
                return 0
            visited.add((r, c))
            length = 1
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                length += dfs(r + dr, c + dc)
            return length
        
        result = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    result = max(result, dfs(r, c))
        return result