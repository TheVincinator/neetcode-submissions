class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        totalFreshFruit = 0
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs():
            minTime = 0
            visitedFreshFruit = 0
            while queue:
                r, c, time = queue.popleft()
                minTime = max(minTime, time)
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (r + dr in range(ROWS) and
                        c + dc in range(COLS) and
                        (r + dr, c + dc) not in visited and
                        grid[r + dr][c + dc] != 0):
                        if grid[r + dr][c + dc] == 1:
                            visitedFreshFruit += 1
                        queue.append((r + dr, c + dc, time + 1))
                        visited.add((r + dr, c + dc))
            return -1 if totalFreshFruit != visitedFreshFruit else minTime

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    totalFreshFruit += 1

        return bfs()