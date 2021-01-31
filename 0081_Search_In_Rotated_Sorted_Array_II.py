""" Binary Search """
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i, j = 0, len(nums) - 1
        while i <= j:
            k = (i + j) // 2
            if nums[k] == target:
                return True
            if nums[k] == nums[j]:
                j -= 1
            elif nums[k] < nums[j]:
                if nums[k] < target <= nums[j]:
                    i = k + 1
                else:
                    j = k - 1
            else:
                if nums[i] <= target < nums[k]:
                    j = k - 1
                else:
                    i = k + 1
        return False


print(Solution().search(nums=[1, 0, 1, 1, 1], target=0))
