""" Math """


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (m + x) % i
        return x


print(Solution().lastRemaining(n=10, m=17))
