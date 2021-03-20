""" Depth-first Search """
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i > 0:
                    dfs(i - 1, j)
                if i + 1 < size[0]:
                    dfs(i + 1, j)
                if j > 0:
                    dfs(i, j - 1)
                if j + 1 < size[1]:
                    dfs(i, j + 1)
                return 1
            return 0

        n, size = 0, (len(grid), len(grid[0]))
        return sum([dfs(i, j) for i in range(size[0]) for j in range(size[1])])


print(Solution().numIslands(
    grid=
    [["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]]
))
