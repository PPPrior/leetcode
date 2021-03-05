""" Dynamic Programming """


class Solution:
    def tribonacci(self, n: int) -> int:
        p, q, r = 0, 1, 1
        for i in range(n):
            p, q, r = q, r, p + q + r
        return p


print(Solution().tribonacci(n=25))
