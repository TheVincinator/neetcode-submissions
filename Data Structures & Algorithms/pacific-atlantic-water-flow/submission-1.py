class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        visited = set()
        pacific = set()
        atlantic = set()
        queue = deque()

        def bfs(ocean):
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (r + dr in range(ROWS) and
                        c + dc in range(COLS) and
                        (r + dr, c + dc) not in visited and
                        heights[r][c] <= heights[r + dr][c + dc]):
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                        ocean.add((r + dr, c + dc))

        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    queue.append((i, j))
                    visited.add((i, j))
                    pacific.add((i, j))

        bfs(pacific)
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if i == ROWS - 1 or j == COLS - 1:
                    queue.append((i, j))
                    visited.add((i, j))
                    atlantic.add((i, j))

        bfs(atlantic)

        result = []
        for (r, c) in pacific:
            if (r, c) in atlantic:
                result.append([r, c])

        return result




         