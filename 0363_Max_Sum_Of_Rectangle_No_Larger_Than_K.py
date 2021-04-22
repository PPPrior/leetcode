""" Binary Search """
from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for up in range(m):
            nums = [0] * n
            for down in range(up, m):
                for i in range(n):
                    nums[i] += matrix[down][i]
                ss, s = SortedList([0]), 0
                for num in nums:
                    s += num
                    p = ss.bisect_left(s - k)
                    if p != len(ss):
                        ans = max(ans, s - ss[p])
                    ss.add(s)
        return ans


print(Solution().maxSumSubmatrix(
    matrix=[[2, 2, -1]],
    k=3
))
