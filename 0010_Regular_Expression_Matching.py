""" Dynamic Programming """


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        def match(i, j):
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != "*":
                    if match(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 2]
                    if match(i, j - 1) and not dp[i][j]:
                        dp[i][j] = dp[i - 1][j]
        return dp[m][n]


print(Solution().isMatch(s="aaa", p="ab*a*c*a"))
