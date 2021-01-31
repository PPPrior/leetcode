""" Binary Search """


class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        while i <= j:
            k = (i + j) // 2
            if k ** 2 > x:
                j = k - 1
            elif (k + 1) ** 2 <= x:
                i = k + 1
            else:
                return k


print(Solution().mySqrt(x=10))
