""" Hash Table """
from typing import List
from collections import defaultdict


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        x1, x2 = 0, 0
        for i in range(1, len(nums) + 1):
            if d[i] == 2:
                x1 = i
            if d[i] == 0:
                x2 = i
        return [x1, x2]


print(Solution().findErrorNums(nums=[1, 2, 2, 4]))
