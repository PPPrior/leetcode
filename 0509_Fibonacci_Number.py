""" Array """


class Solution:
    def fib(self, n: int) -> int:
        p, q = 0, 1
        for i in range(n):
            p, q = q, p + q
        return p


print(Solution().fib(n=3))
