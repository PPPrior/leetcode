""" Depth-first Search """
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if grid[i][j]:
                grid[i][j], s = 0, 0
                s += dfs(i - 1, j) if i > 0 else 0
                s += dfs(i + 1, j) if i < size[0] - 1 else 0
                s += dfs(i, j - 1) if j > 0 else 0
                s += dfs(i, j + 1) if j < size[1] - 1 else 0
                return s + 1
            return 0

        size = (len(grid), len(grid[0]))  # (row, col)
        ans = 0
        for i in range(size[0]):
            for j in range(size[1]):
                ans = max(ans, dfs(i, j))
        return ans


print(Solution().maxAreaOfIsland(
    grid=
    [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
))
