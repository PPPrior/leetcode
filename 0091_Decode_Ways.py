""" Dynamic Programming """


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [1]
        for i in range(1, n):
            if s[i] == "0":
                if 0 < int(s[i - 1]) <= 2:
                    dp.append(dp[i - 2])
                else:
                    return 0
            else:
                if 10 < int(s[i - 1:i + 1]) <= 26:
                    if i > 1:
                        dp.append(dp[-1] + dp[-2])
                    else:
                        dp.append(dp[-1] + 1)
                else:
                    dp.append(dp[-1])
        return dp[-1]


print(Solution().numDecodings(s="10"))
