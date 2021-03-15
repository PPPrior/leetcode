""" Array """
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = list()

        def circle(matrix, ans):
            ans += matrix[0]
            ans += [row[-1] for row in matrix][1:-1]
            if len(matrix) > 1:
                ans += matrix[-1][::-1]
            if len(matrix[0]) > 1:
                ans += [row[0] for row in matrix[::-1]][1:-1]

        while matrix and matrix[0]:
            circle(matrix, ans)
            matrix = [row[1:-1] for row in matrix[1:-1]]
        return ans


print(Solution().spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
