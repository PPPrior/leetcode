""" Dynamic Programming """


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for s in range(1, k):
                        if dp[i][j][s] and dp[i + s][j + s][k - s]:
                            dp[i][j][k] = True
                            break
                        if dp[i][j + k - s][s] and dp[i + s][j][k - s]:
                            dp[i][j][k] = True
                            break
        return dp[0][0][n]


print(Solution().isScramble(s1="great", s2="rgeat"))
