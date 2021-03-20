""" Backtracking """


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row=0):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in column or row + col in diagonal1 or row - col in diagonal2:
                    continue
                column.add(col)
                diagonal1.add(row + col)
                diagonal2.add(row - col)
                count += backtrack(row + 1)
                column.remove(col)
                diagonal1.remove(row + col)
                diagonal2.remove(row - col)
            return count

        column, diagonal1, diagonal2 = set(), set(), set()
        return backtrack()


print(Solution().totalNQueens(n=8))
