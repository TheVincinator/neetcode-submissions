class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruits = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruits += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))

        time = 0
        while queue:
            r, c, t = queue.popleft()
            time = t
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_r = r + dr
                new_c = c + dc
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or grid[new_r][new_c] == 0 or grid[new_r][new_c] == 2:
                    continue
                queue.append((new_r, new_c, t + 1))
                grid[new_r][new_c] = 2
                freshFruits -= 1

        return -1 if freshFruits != 0 else time