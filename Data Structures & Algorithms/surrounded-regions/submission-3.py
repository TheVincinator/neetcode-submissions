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

        for r in range(len(board)):
            for c in range(len(board[0])):
                if ((r == 0 
                    or r == len(board) - 1 
                    or c == 0 
                    or c == len(board[0]) - 1) 
                    and board[r][c] == "O" 
                    and (r, c) not in visited):
                    dfs(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    continue
                if (r, c) in visited:
                    continue
                board[r][c] = "X"