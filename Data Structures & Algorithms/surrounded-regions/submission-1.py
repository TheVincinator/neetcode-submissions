class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1) and board[i][j] == "O":
                    visited.add((i, j))
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (r + dr in range(ROWS) and
                    c + dc in range(COLS) and
                    (r + dr, c + dc) not in visited and
                    board[r + dr][c + dc] == "O"):
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in visited:
                    print(board[i][j])
                    board[i][j] = "X"