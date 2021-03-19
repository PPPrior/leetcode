""" Two Pointers """
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, i = len(nums), 0
        p0, p2 = 0, n - 1
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
            i += 1


Solution().sortColors(nums=[1, 2, 0])
