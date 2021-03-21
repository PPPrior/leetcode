""" Array """
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0] * n for _ in range(n)]
        num, m = 1, n * n
        while num <= m:
            # left --> right
            for i in range(l, r + 1):
                mat[t][i] = num
                num += 1
            t += 1
            # top --> bottom
            for i in range(t, b + 1):
                mat[i][r] = num
                num += 1
            r -= 1
            # right --> left
            for i in range(r, l - 1, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            # bottom --> top
            for i in range(b, t - 1, -1):
                mat[i][l] = num
                num += 1
            l += 1
        return mat


print(Solution().generateMatrix(n=4))
