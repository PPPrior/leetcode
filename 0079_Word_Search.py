""" Backtracking """
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            for dir in dirs:
                x, y = i + dir[0], j + dir[1]
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if dfs(x, y, k + 1):
                        return True
            visited.remove((i, j))
            return False

        m, n = len(board), len(board[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


print(Solution().exist(
    board=[["A", "B", "C", "E"],
           ["S", "F", "C", "S"],
           ["A", "D", "E", "E"]],
    word="ABCB"
))
