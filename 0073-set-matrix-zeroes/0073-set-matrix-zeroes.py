class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp_mat = [row[:] for row in matrix]
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for k in range(cols):
                        temp_mat[i][k] = 0
                    for l in range(rows):
                        temp_mat[l][j] = 0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = temp_mat[i][j]