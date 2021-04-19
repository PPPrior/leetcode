""" Two Pointers """
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p


print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
