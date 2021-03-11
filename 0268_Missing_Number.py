""" Math """
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


print(Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
