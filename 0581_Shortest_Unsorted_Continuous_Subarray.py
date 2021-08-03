""" Array """
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, minn = float('-inf'), float('inf')
        left, right = -1, -1
        for i in range(n):
            if maxn <= nums[i]:
                maxn = nums[i]
            else:
                right = i
            if minn >= nums[n - i - 1]:
                minn = nums[n - i - 1]
            else:
                left = n - i - 1
        return 0 if right == -1 else right - left + 1


print(Solution().findUnsortedSubarray(nums=[2, 6, 4, 8, 10, 9, 15]))
