""" Bit Manipulation """


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:0>32b}'[::-1], 2)


print(Solution().reverseBits(n=43261596))
