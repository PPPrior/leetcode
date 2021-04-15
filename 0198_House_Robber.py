""" Dynamic Programming """
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        n = len(nums)
        if n <= 2:
            return max(nums)
        x, y = nums[0], max(nums[:2])
        for i in range(2, n):
            x, y = y, max(x + nums[i], y)
        return y


print(Solution().rob(nums=[2, 7, 9, 3, 1]))
