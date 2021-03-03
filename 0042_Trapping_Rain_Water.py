""" Greedy """
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n, s = len(height), 0
        # left --> right
        c, l = 0, 0
        for r in range(1, n):
            if height[r] < height[l]:
                c += height[r]
            else:
                s += height[l] * (r - l - 1) - c
                l, c = r, 0
        # left <-- right
        c, r = 0, n - 1
        for l in range(n - 2, -1, -1):
            if height[l] <= height[r]:
                c += height[l]
            else:
                s += height[r] * (r - l - 1) - c
                r, c = l, 0
        return s


print(Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
