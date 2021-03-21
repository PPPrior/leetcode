""" Backtracking """
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(array, left, right):
            if len(array) == n * 2:
                ans.append("".join(array))
                return
            if left < n:
                array.append('(')
                backtrack(array, left + 1, right)
                array.pop()
            if right < left:
                array.append(')')
                backtrack(array, left, right + 1)
                array.pop()

        ans = []
        backtrack([], 0, 0)
        return ans


print(Solution().generateParenthesis(n=3))
