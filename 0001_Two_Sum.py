""" Hash Table """
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            else:
                d[num] = i


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
