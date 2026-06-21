class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        def dfs(i, j):
            if ((i < 0 or i >= len(grid))
                or (j < 0 or j >= len(grid[0]))
                or (i, j) in visited
                or grid[i][j] == "0"):
                return
            visited.add((i, j))
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(i + di, j + dj)
            
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        return result