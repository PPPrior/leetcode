""" Dynamic Programming """


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ''
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans

    """ Center Spread """
    """
    def longestPalindrome(self, s: str) -> str:
        def centerSpread(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j], j - i - 1

        ans = ''
        for i in range(len(s)):
            s1, n1 = centerSpread(i, i)
            s2, n2 = centerSpread(i, i + 1)
            if n1 > n2 and n1 > len(ans):
                ans = s1
            elif n2 > n1 and n2 > len(ans):
                ans = s2
        return ans
    """


print(Solution().longestPalindrome(s="babad"))
