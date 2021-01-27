""" Dynamic Programming """
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        m = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
        dp = [0]
        for i in range(1, n + 1):
            dp.append(min(dp[i - j] for j in m if j <= i) + 1)
        return dp[-1]


print(Solution().numSquares(40))
