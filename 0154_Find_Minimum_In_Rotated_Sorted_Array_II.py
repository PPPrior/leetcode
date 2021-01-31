""" Binary Search """
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            k = (i + j) // 2
            if nums[k] == nums[j]:
                j -= 1
            elif nums[k] < nums[j]:
                j = k
            else:
                i = k + 1
        return nums[i]


print(Solution().findMin([5, 1, 3, 3, 3]))
