class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for r in row:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0
                

        