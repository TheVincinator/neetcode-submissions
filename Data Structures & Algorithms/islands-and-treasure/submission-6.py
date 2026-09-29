class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            r, c, dist = queue.popleft()
            grid[r][c] = dist
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_r, new_c = r + dr, c + dc
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or grid[new_r][new_c] == -1 or (new_r, new_c) in visited:
                    continue
                queue.append((new_r, new_c, dist + 1))
                visited.add((new_r, new_c))