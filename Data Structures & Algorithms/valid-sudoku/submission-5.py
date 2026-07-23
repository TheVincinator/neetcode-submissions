class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    row.append(board[i][j])
            if len(row) != len(set(row)):
                return False

        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != ".":
                    col.append(board[j][i])
            if len(col) != len(set(col)):
                return False

        grid = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    grid[i // 3 * 3 + j // 3].append(board[i][j])
        
        for box in grid:
            if len(box) != len(set(box)):
                return False
        return True

