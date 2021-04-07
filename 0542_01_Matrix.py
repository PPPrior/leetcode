""" Dynamic Programming """
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def search(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return float('inf')
            return matrix[i][j]

        m, n = len(matrix), len(matrix[0])
        # top left --> bottom right
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 1 + min(search(i - 1, j), search(i, j - 1))
        # bottom right ---> top left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    matrix[i][j] = min(matrix[i][j], 1 + min(search(i + 1, j), search(i, j + 1)))
        return matrix


print(Solution().updateMatrix(
    matrix=
    [[0, 0, 1, 0, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 1, 1, 1, 0],
     [0, 0, 1, 0, 0]]
))
