""" Bit Manipulation """
from typing import List
from functools import reduce
from operator import xor


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        q = reduce(xor, range(1, n + 1))
        for i in range(1, n - 1, 2):
            q ^= encoded[i]
        ans = [q]
        for i in range(n - 1):
            ans.append(ans[-1] ^ encoded[i])
        return ans


print(Solution().decode(encoded=[6, 5, 4, 6]))
