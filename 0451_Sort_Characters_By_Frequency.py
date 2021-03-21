""" Hash Table """
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        d, ans = defaultdict(int), []
        for ch in s:
            d[ch] += 1
        buckets = [[] for _ in range(len(s) + 1)]
        for k, v in d.items():
            buckets[v].append(k)
        for i in range(len(s), 0, -1):
            ans += [x * i for x in buckets[i]]
        return "".join(ans)


print(Solution().frequencySort(s="tree"))
