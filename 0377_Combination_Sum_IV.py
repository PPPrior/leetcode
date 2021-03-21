""" Dynamic Programming """
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            dp[i] = sum([dp[i - n] for n in nums if i >= n])
        return dp[target]


print(Solution().combinationSum4(nums=[1, 2, 3], target=4))
