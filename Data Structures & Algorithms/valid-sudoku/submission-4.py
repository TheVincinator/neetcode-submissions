class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            lst = []
            for cell in row:
                if cell != ".":
                    lst.append(cell)
            if len(lst) != len(set(lst)):
                return False
        for i in range(len(board)):
            lst = []
            for j in range(len(board[i])):
                if board[j][i] != ".":
                    lst.append(board[j][i])
            if len(lst) != len(set(lst)):
                return False
        boxes = [[] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    box = (i // 3) * 3 + (j // 3)
                    boxes[box].append(board[i][j])
        for box in boxes:
            if len(box) != len(set(box)):
                return False
        return True

