""" Binary Search """
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            k = (i + j) // 2
            if nums[k] < nums[j]:
                j = k
            else:
                i = k + 1
        return nums[i]


print(Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
