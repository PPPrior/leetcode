""" Dynamic Programming """
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        p = [0] * m
        dp = [1] * n
        for i in range(1, n):
            dp[i] = min(dp[p[j]] * primes[j] for j in range(m))
            for j in range(m):
                if dp[i] == dp[p[j]] * primes[j]:
                    p[j] += 1
        return dp[-1]


print(Solution().nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))
