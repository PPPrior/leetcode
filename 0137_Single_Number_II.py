""" Hash Table """
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return [k for k, v in c.items() if v == 1][0]


print(Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]))
