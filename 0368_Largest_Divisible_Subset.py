""" Dynamic Programming """
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[x] for x in nums]
        for i in range(len(nums)):
            for j in range(i):
                if not nums[i] % nums[j] and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)


print(Solution().largestDivisibleSubset(nums=[2, 3, 4, 9, 8]))
