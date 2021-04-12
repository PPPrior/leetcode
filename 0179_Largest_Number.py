""" Sort Algorithm """
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
        return "".join(s) if s[0] != "0" else "0"


print(Solution().largestNumber(nums=[3, 30, 34, 5, 9]))
