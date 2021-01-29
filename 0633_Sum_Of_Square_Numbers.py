""" Two Pointers """
from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n, m = 0, int(sqrt(c))
        while n <= m:
            k = n * n + m * m
            if k < c:
                n += 1
            elif k > c:
                m -= 1
            else:
                return True
        return False


print(Solution().judgeSquareSum(c=3))
