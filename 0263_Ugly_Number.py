""" Math """


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while not n % factor:
                n //= factor
        return n == 1


print(Solution().isUgly(n=8))
