""" Binary Search """
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        d = []
        for i in range(n):
            if not d or envelopes[i][1] > d[-1][1]:
                d.append(envelopes[i])
            else:
                l, r = 0, len(d) - 1
                while l < r:
                    m = (l + r) // 2
                    if envelopes[i][1] <= d[m][1]:
                        r = m
                    else:
                        l = m + 1
                d[r] = envelopes[i]
        return len(d)


print(Solution().maxEnvelopes(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]]))
