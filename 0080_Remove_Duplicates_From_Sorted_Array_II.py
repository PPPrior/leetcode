""" Two Pointers """
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


print(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
