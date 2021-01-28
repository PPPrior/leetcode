""" Two Pointers """
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {k: v for v, k in enumerate(S)}
        ans = []
        l = r = 0
        for i, s in enumerate(S):
            r = max(r, d[s])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans


print(Solution().partitionLabels(S="ababcbacadefegdehijhklij"))
