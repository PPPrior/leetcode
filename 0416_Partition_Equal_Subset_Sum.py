""" Dynamic Programming """
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1:
            return False
        target //= 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(target, nums[i - 1] - 1, -1):
                dp[j] = (dp[j] | dp[j - nums[i - 1]])
        return dp[target]


print(Solution().canPartition(nums=[1, 5, 10, 6]))
