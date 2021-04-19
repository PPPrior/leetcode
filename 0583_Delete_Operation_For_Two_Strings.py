""" Dynamic Programming """


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        for i in range(m + 1):
            temp = [0] * (n + 1)
            for j in range(n + 1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = min(temp[j - 1], dp[j]) + 1
            dp = temp
        return dp[n]


print(Solution().minDistance(word1="leetcode", word2="etco"))
