""" Dynamic Programming """


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        col = min(steps, arrLen - 1)
        dp = [0] * (col + 1)
        dp[0] = 1
        for i in range(1, steps + 1):
            temp = [0] * (col + 1)
            for j in range(col + 1):
                temp[j] = dp[j]
                if j - 1 >= 0:
                    temp[j] = temp[j] + dp[j - 1]
                if j + 1 <= col:
                    temp[j] = temp[j] + dp[j + 1]
                temp[j] %= mod
            dp = temp
        return dp[0]


print(Solution().numWays(steps=3, arrLen=2))
