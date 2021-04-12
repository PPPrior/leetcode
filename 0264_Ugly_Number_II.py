""" Dynamic Programming """


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        p1, p2, p3 = 0, 0, 0
        for i in range(1, n):
            c1, c2, c3 = dp[p1] * 2, dp[p2] * 3, dp[p3] * 5
            dp[i] = min(c1, c2, c3)
            if dp[i] == c1:
                p1 += 1
            if dp[i] == c2:
                p2 += 1
            if dp[i] == c3:
                p3 += 1
        return dp[-1]


print(Solution().nthUglyNumber(n=10))
