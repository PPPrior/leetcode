""" Math """


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans, pre = 0, d[s[0]]
        for i in range(1, len(s)):
            ans += pre if pre >= d[s[i]] else -pre
            pre = d[s[i]]
        ans += pre
        return ans


print(Solution().romanToInt(s="IV"))
