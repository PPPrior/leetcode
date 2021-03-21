""" Backtracking """
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        ans, tmp = list(), list()

        def backtrack(i):
            if i == n:
                ans.append(tmp[:])
            for j in range(i, n):
                if dp[i][j]:
                    tmp.append(s[i:j + 1])
                    backtrack(j + 1)
                    tmp.pop()

        backtrack(0)
        return ans


print(Solution().partition(s="aab"))
