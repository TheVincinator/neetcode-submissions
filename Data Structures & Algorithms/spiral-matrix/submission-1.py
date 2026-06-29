class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # [1, 2, 3, 4]
        # [5, 6, 7, 8]
        # [9, 0, 1, 2]
        # [3, 4, 5, 6]
        result = []
        t = 0
        r = len(matrix[0])
        l = 0
        b = len(matrix)
        while l < r and t < b:
            for i in range(l, r):
                result.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                result.append(matrix[i][r - 1])
            r -= 1
            if not (l < r and t < b):
                break
            for i in range(r - 1, l - 1, -1):
                result.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, t - 1, -1):
                result.append(matrix[i][l])
            l += 1
        return result
