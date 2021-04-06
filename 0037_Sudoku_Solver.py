""" Backtracking """
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(blank):
            nonlocal valid
            if not blank:
                valid = True
                return
            i, j = blank.pop()
            choice = nums - (row[i] | col[j] | grid[i // 3][j // 3])
            for num in choice:
                row[i].add(num)
                col[j].add(num)
                grid[i // 3][j // 3].add(num)
                board[i][j] = num
                backtrack(blank)
                if valid:
                    return
                row[i].remove(num)
                col[j].remove(num)
                grid[i // 3][j // 3].remove(num)
                board[i][j] = "."
            blank.append((i, j))

        nums = {str(x) for x in range(1, 10)}
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [[set() for _ in range(3)] for _ in range(3)]
        blank = []
        valid = False
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    grid[i // 3][j // 3].add(board[i][j])
                else:
                    blank.append((i, j))

        backtrack(blank)


Solution().solveSudoku(
    board=
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
)
