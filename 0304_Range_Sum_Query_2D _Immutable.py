""" Dynamic Programming """
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = 0, 0
        if matrix and matrix[0]:
            m, n = len(matrix), len(matrix[0])

        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.preSum[i + 1][j + 1] = matrix[i][j] + self.preSum[i][j + 1] + \
                                            self.preSum[i + 1][j] - self.preSum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] + self.preSum[row1][col1] - self.preSum[row1][col2 + 1] - \
               self.preSum[row2 + 1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
