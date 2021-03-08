""" Backtracing """


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        ns = [float('inf')] * n
        for i in range(n):
            if dp[0][i]:
                ns[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        ns[i] = min(ns[i], ns[j] + 1)
        return int(ns[-1])


print(Solution().minCut(s="aab"))
