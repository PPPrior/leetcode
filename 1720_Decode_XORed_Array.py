""" Bit Manipulation """
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for num in encoded:
            arr.append(num ^ arr[-1])
        return arr


print(Solution().decode(encoded=[1, 2, 3], first=1))
