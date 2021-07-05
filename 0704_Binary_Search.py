""" Binary Search """
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid
        return -1


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9))
