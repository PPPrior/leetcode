""" Dynamic Programming """


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = max(max(dp[i - j] * j, (i - j) * j) for j in range(1, i))
        return dp[n]


print(Solution().integerBreak(n=10))
