""" Dynamic Programming """


class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i]=dp[i-1]+dp[i-2]
        p, q = 0, 1
        for i in range(n):
            p, q = q, p + q
        return q


print(Solution().climbStairs(n=3))
