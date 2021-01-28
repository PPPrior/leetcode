""" Bit Manipulation """
from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


print(Solution().singleNumber(nums=[5, 1, 2, 1, 2]))
