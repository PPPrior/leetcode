""" Binary Search """
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findrow():
            i0, i1 = 0, m - 1
            while i0 < i1:
                k = (i0 + i1) // 2
                if target < matrix[k][0]:
                    i1 = k - 1
                elif target > matrix[k][-1]:
                    i0 = k + 1
                else:
                    return k
            return i0

        def findcol(i):
            j0, j1 = 0, n - 1
            while j0 < j1:
                k = (j0 + j1) // 2
                if target < matrix[i][k]:
                    j1 = k - 1
                elif target > matrix[i][k]:
                    j0 = k + 1
                else:
                    return k
            return j0

        m, n = len(matrix), len(matrix[0])
        i = findrow()
        j = findcol(i)
        return target == matrix[i][j]


print(Solution().searchMatrix(
    matrix=[[-9, -7, -7, -5, -3],
            [-1, 0, 1, 3, 3],
            [5, 7, 9, 11, 12],
            [13, 14, 15, 16, 18],
            [19, 21, 22, 22, 22]],
    target=1))
