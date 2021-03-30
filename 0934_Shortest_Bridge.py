""" Breadth-first Search """
from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            if A[i][j] != 1:
                return
            ps.append((i, j))
            A[i][j] = 2
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        def bfs():
            ans = 0
            while ps:
                c = len(ps)
                for _ in range(c):
                    i, j = ps.pop(0)
                    for d in dirs:
                        x, y = i + d[0], j + d[1]
                        if not (0 <= x < m and 0 <= y < n):
                            continue
                        if A[x][y] == 2:
                            continue
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            ps.append((x, y))
                        elif A[x][y] == 1:
                            return ans
                ans += 1

        m, n = len(A), len(A[0])
        ps = list()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        flag = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j)
                    flag = True
                    break
            if flag:
                break
        return bfs()


print(Solution().shortestBridge(
    A=[[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 1, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]
))
