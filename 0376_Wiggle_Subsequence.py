""" Dynamic Programming """
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up, down = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = max(down + 1, up)
            elif nums[i] < nums[i - 1]:
                down = max(up + 1, down)
        return max(up, down)


print(Solution().wiggleMaxLength(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]))
