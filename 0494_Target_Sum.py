""" Dynamic Programming """
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target or (s + target) & 1:
            return 0
        target = (s + target) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        return dp[-1]


print(Solution().findTargetSumWays(nums=[0, 0, 0, 0, 0, 0, 0, 0, 1], target=1))
