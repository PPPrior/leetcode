""" Depth-first Search """
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            if isConnected[i][i] == 0:
                return 0
            isConnected[i][i] = 0
            for j in range(n):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = isConnected[j][i] = 0
                    dfs(j)
            return 1

        n = len(isConnected)
        ans = 0
        for i in range(n):
            ans += dfs(i)
        return ans


print(Solution().findCircleNum(
    isConnected=
    [[1, 0, 0, 1],
     [0, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 0, 1, 1]]
))
