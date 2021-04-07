""" Dynamic Programming """
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        m, n = len(matrix), len(matrix[0])
        w = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    w = max(w, dp[i][j])
        return w * w


print(Solution().maximalSquare(
    matrix=
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]
))
