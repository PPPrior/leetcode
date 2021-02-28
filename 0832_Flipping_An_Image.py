""" Array """
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[x ^ 1 for x in row[::-1]] for row in A]


print(Solution().flipAndInvertImage(A=[[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
