class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()

        def bfs():
            while queue:
                row, col, length = queue.popleft()
                if grid[row][col] != 0:
                    grid[row][col] = length
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (row + dr in range(len(grid)) and 
                    col + dc in range(len(grid[0])) and 
                    (row + dr, col + dc) not in visited and
                    grid[row + dr][col + dc] != -1):
                        visited.add((row + dr, col + dc))
                        queue.append((row + dr, col + dc, length + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        bfs()
            