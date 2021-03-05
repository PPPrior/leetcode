""" Dynamic Programming """


class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[n]=dp[n-1]+dp[n-2]
        p, q = 0, 1
        for i in range(n):
            p, q = q, p + q
        return q


print(Solution().climbStairs(n=3))
