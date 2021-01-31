""" Binary Search """
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, left):
            i, j, p = 0, len(nums), -1
            while i <= j:
                k = (i + j) // 2
                if nums[k] == target:
                    p = k
                    if left:
                        j = k - 1
                    else:
                        i = k + 1
                elif nums[k] < target:
                    i = k + 1
                else:
                    j = k - 1
            return p

        return [binarySearch(nums, target, True), binarySearch(nums, target, False)]


print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
