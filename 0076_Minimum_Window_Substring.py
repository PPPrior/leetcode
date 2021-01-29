""" Two Pointers """
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for ch in t:
            d[ch] += 1
        p1, cnt, ans = 0, len(t), (0, float('inf'))
        for p2, ch in enumerate(s):
            if d[ch] > 0:
                cnt -= 1
            d[ch] -= 1
            if cnt == 0:
                while d[s[p1]] < 0:
                    d[s[p1]] += 1
                    p1 += 1
                if p2 - p1 < ans[1] - ans[0]:
                    ans = (p1, p2)
                d[s[p1]] += 1
                cnt += 1
                p1 += 1
        return '' if ans[1] > len(s) else s[ans[0]:ans[1] + 1]


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
