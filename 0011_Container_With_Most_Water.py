""" Two Pointers """
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, s = 0, len(height) - 1, 0
        while i < j:
            s = max(s, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return s


print(Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
