""" Divide and Conquer """
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(lo, hi):
            pivot = nums[lo]
            while lo < hi:
                while lo < hi and nums[hi] >= pivot:
                    hi -= 1
                nums[lo] = nums[hi]
                while lo < hi and nums[lo] <= pivot:
                    lo += 1
                nums[hi] = nums[lo]
            nums[lo] = pivot
            return lo

        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            p = partition(lo, hi)
            if p == n - k:
                return nums[p]
            elif p > n - k:
                hi = p - 1
            else:
                lo = p + 1


print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
