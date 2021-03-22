""" Depth-first Search """
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        def dfs(i, j, ocean):
            if ocean[i][j]:
                return
            ocean[i][j] = True
            for flow in flows:
                x, y = i + flow[0], j + flow[1]
                if not (0 <= x < m and 0 <= y < n):
                    continue
                if matrix[i][j] > matrix[x][y]:
                    continue
                dfs(x, y, ocean)

        m, n = len(matrix), len(matrix[0])
        pacific = [[False] * n for _ in range(m)]  # can flow to pacific ?
        atlantic = [[False] * n for _ in range(m)]  # can flow to atlantic ?
        flows = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # four directions (up, down, left, right)
        ans = list()

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans


print(Solution().pacificAtlantic(
    matrix=
    [[1, 2, 2, 3, 5],
     [3, 2, 3, 4, 4],
     [2, 4, 5, 3, 1],
     [6, 7, 1, 4, 5],
     [5, 1, 1, 2, 4]]
))
