""" Binary Search """
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
            lo, hi = max(weights), sum(weights)
            while lo < hi:
                mid = (lo + hi) // 2
                temp, day = 0, 1
                for weight in weights:
                    temp += weight
                    if temp > mid:
                        day += 1
                        temp = weight
                if day > D:
                    lo = mid + 1
                else:
                    hi = mid
            return lo


print(Solution().shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], D=5))
