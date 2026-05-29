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
        boxes = [[],[],[],[],[],[],[],[],[]]
        for i in range(len(board)):
            for j in range(len(board)):
                if i <= 2 and j <= 2 and board[i][j] != ".":
                    boxes[0].append(board[i][j])
                elif i <= 2 and 3 <= j <= 5 and board[i][j] != ".":
                    boxes[1].append(board[i][j])
                elif i <= 2 and 6 <= j and board[i][j] != ".":
                    boxes[2].append(board[i][j])
                elif 3 <= i <= 5 and j <= 2 and board[i][j] != ".":
                    boxes[3].append(board[i][j])
                elif 3 <= i <= 5 and 3 <= j <= 5 and board[i][j] != ".":
                    boxes[4].append(board[i][j])
                elif 3 <= i <= 5 and 6 <= j and board[i][j] != ".":
                    boxes[5].append(board[i][j])
                elif 6 <= i and j <= 2 and board[i][j] != ".":
                    boxes[6].append(board[i][j])
                elif 6 <= i and 3 <= j <= 5 and board[i][j] != ".":
                    boxes[7].append(board[i][j])
                elif 6 <= i and 6 <= j and board[i][j] != ".":
                    boxes[8].append(board[i][j])
        for box in boxes:
            if len(box) != len(set(box)):
                return False
        return True

