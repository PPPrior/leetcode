""" Sort Algorithm """
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        buckets, size = dict(), t + 1
        for i, n in enumerate(nums):
            id = n // size
            if id in buckets:
                return True
            if (id - 1) in buckets and abs(n - buckets[id - 1]) <= t:
                return True
            if (id + 1) in buckets and abs(n - buckets[id + 1]) <= t:
                return True
            buckets[id] = n
            if i >= k:
                buckets.pop(nums[i - k] // size)
        return False


print(Solution().containsNearbyAlmostDuplicate(nums=[0, 5, 0], k=2, t=4))
