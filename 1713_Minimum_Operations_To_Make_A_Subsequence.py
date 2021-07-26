""" Binary Search """
from typing import List
from bisect import bisect_left


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        pos = {}
        for i, v in enumerate(target):
            pos[v] = i
        d = []
        for val in arr:
            if val in pos:
                idx = pos[val]
                p = bisect_left(d, idx)
                if p < len(d):
                    d[p] = idx
                else:
                    d.append(idx)
        return n - len(d)


print(Solution().minOperations(target=[6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1]))
