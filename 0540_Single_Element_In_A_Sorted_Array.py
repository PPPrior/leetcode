""" Binary Search """
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            k = (i + j) // 2
            if (k & 1) ^ (nums[k] == nums[k + 1]):
                i = k + 1
            else:
                j = k
        return nums[j]


print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
