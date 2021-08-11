""" Dynamic Programming """
from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        for i, num in enumerate(nums):
            for j in range(i):
                d = num - nums[j]
                cnt = dp[j][d]
                ans += cnt
                dp[i][d] += cnt + 1
        return ans


print(Solution().numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
