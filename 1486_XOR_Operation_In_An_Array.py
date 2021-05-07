""" Bit Manipulation """


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= (start + i * 2)
        return ans


print(Solution().xorOperation(n=4, start=3))
