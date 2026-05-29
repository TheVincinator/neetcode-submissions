class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for row in board:
            lst = []
            for cell in row:
                if cell in nums:
                    lst.append(cell)
            if len(lst) != len(set(lst)):
                return False
        for i in range(len(board)):
            lst = []
            for j in range(len(board[i])):
                if board[j][i] in nums:
                    lst.append(board[j][i])
            if len(lst) != len(set(lst)):
                return False
        boxes = [[],[],[],[],[],[],[],[],[]]
        for i in range(len(board)):
            for j in range(len(board)):
                if i <= 2 and j <= 2 and board[i][j] in nums:
                    boxes[0].append(board[i][j])
                elif i <= 2 and 3 <= j <= 5 and board[i][j] in nums:
                    boxes[1].append(board[i][j])
                elif i <= 2 and 6 <= j <= 8 and board[i][j] in nums:
                    boxes[2].append(board[i][j])
                elif 3 <= i <= 5 and j <= 2 and board[i][j] in nums:
                    boxes[3].append(board[i][j])
                elif 3 <= i <= 5 and 3 <= j <= 5 and board[i][j] in nums:
                    boxes[4].append(board[i][j])
                elif 3 <= i <= 5 and 6 <= j <= 8 and board[i][j] in nums:
                    boxes[5].append(board[i][j])
                elif 6 <= j <= 8 and j <= 2 and board[i][j] in nums:
                    boxes[6].append(board[i][j])
                elif 6 <= j <= 8 and 3 <= j <= 5 and board[i][j] in nums:
                    boxes[7].append(board[i][j])
                elif 6 <= j <= 8 and 6 <= j <= 8 and board[i][j] in nums:
                    boxes[8].append(board[i][j])
        for box in boxes:
            if len(box) != len(set(box)):
                return False
        return True

