""" Hash Table """
from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d, n, ans = defaultdict(int), len(nums), list()
        for num in nums:
            d[num] += 1
        # Bucket Sort
        buckets = [[] for _ in range(n + 1)]
        for key, val in d.items():
            buckets[val].append(key)
        for bucket in buckets[::-1]:
            ans += bucket if bucket else []
        return ans[:k]


print(Solution().topKFrequent(nums=[1, 2], k=2))
