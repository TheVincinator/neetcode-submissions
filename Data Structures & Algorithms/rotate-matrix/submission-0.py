class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        h = 0
        for i in range(len(matrix)):
            for j in range(h, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print(matrix)
            h += 1