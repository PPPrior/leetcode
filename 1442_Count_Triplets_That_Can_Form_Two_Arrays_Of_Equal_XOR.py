""" Bit Manipulation """
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 1):
            num = arr[i]
            for j in range(i + 1, n):
                num ^= arr[j]
                if num == 0:
                    ans += j - i
        return ans


print(Solution().countTriplets(arr=[1, 1, 1, 1, 1]))
