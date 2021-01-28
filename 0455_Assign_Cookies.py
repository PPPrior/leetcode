""" Greedy """
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        count, i, j = 0, 0, 0
        while i < n and j < m:
            if g[i] > s[j]:
                j += 1
            else:
                count += 1
                i += 1
                j += 1
        return count


print(Solution().findContentChildren(g=[3, 2, 1], s=[1, 1]))
