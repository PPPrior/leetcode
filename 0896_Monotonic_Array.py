""" Array """
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = dec = True
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                dec = False
            if A[i] > A[i + 1]:
                inc = False
        return inc or dec


print(Solution().isMonotonic(A=[1, 2, 4, 5]))
