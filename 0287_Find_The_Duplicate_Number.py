""" Binary Search """
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, j = 1, len(nums)
        while i < j:
            k = (i + j) // 2
            c = 0
            for num in nums:
                if num <= k:
                    c += 1
            if c > k:
                j = k
            else:
                i = k + 1
        return i


print(Solution().findDuplicate(nums=[1, 3, 4, 2, 2]))
