class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        for i in range(len(grid)):
            row = []
            for _ in range(len(grid[i])):
                row.append(False)
            visited.append(row)
        
        def dfs(i, j):
            if ((i < 0 or i >= len(grid))
                or (j < 0 or j >= len(grid[0]))
                or visited[i][j]
                or grid[i][j] == "0"):
                return
            visited[i][j] = True
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(i + di, j + dj)
            
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        return result