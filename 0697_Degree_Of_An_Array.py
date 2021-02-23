""" Array """
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                d[num][0] += 1
                d[num][2] = i
            else:
                d[num] = [1, i, i]
        degree, length = 0, len(nums)
        for n, left, right in d.values():
            temp = right - left + 1
            if n > degree:
                degree = n
                length = temp
            elif n == degree:
                length = min(length, temp)
        return length


print(Solution().findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2]))
