""" Dynamic Programming """


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(2, i):
                if not i % j:
                    dp[i] = dp[i // j] + j
                    break
        return dp[n]


print(Solution().minSteps(n=15))
