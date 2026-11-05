class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                r_n = r + dr
                c_n = c + dc
                if (r_n >= 0 
                    and r_n < ROWS 
                    and c_n >= 0 
                    and c_n < COLS 
                    and board[r_n][c_n] == "O" 
                    and (r_n, c_n) not in visited):
                    dfs(r_n, c_n)

        for r in range(ROWS):
            for c in range(COLS):
                if ((r == 0 
                    or r == ROWS - 1 
                    or c == 0 
                    or c == COLS - 1) 
                    and board[r][c] == "O" 
                    and (r, c) not in visited):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    continue
                if (r, c) in visited:
                    continue
                board[r][c] = "X"