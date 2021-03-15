""" Hash Table """
from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        d = sorted(d.items(), key=lambda x: -x[1])
        return [x[0] for x in d[:k]]


print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 2, 2, 3], k=2))
