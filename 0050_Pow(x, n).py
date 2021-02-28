""" Binary Search """


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1
            else:
                t = fastPow(x, n // 2)
                return t * t * x if n & 1 else t * t

        return fastPow(x, n) if n > 0 else 1 / fastPow(x, -n)


print(Solution().myPow(x=2.00000, n=-10))
