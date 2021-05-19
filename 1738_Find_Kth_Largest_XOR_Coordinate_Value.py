""" Dynamic Programming """
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        results = []
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] ^ dp[i][j - 1] ^ dp[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                results.append(dp[i][j])

        results.sort(reverse=True)
        return results[k - 1]


print(Solution().kthLargestValue(
    matrix=[[5, 2],
            [1, 6]],
    k=2))
