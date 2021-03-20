""" Backtracking """
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def addQueen(row, col):
            column.add(col)
            diagonal1.add(row + col)
            diagonal2.add(row - col)

        def removeQueen(row, col):
            column.remove(col)
            diagonal1.remove(row + col)
            diagonal2.remove(row - col)

        def getBoard():
            board = [["."] * n for _ in range(n)]
            for i in range(n):
                board[i][queen[i]] = "Q"
                board[i] = "".join(board[i])
            ans.append(board)

        def backtrack(row):
            if row == n:
                getBoard()
                return
            for col in range(n):
                if col in column or row + col in diagonal1 or row - col in diagonal2:
                    continue
                queen[row] = col
                addQueen(row, col)
                backtrack(row + 1)
                removeQueen(row, col)

        queen = [-1] * n
        column, diagonal1, diagonal2 = set(), set(), set()
        ans = list()
        backtrack(0)
        return ans


print(Solution().solveNQueens(n=8))
