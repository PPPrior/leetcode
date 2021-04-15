""" Dynamic Programming """
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        def houseRobber(ns):
            x, y = ns[0], max(ns[:2])
            for i in range(2, len(ns)):
                x, y = y, max(y, x + ns[i])
            return y

        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))


print(Solution().rob(nums=[1, 2, 3, 1]))
