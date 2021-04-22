""" Divide and Conquer """
from typing import List
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    temp = nums[i] * nums[k] * nums[j]
                    temp += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], temp)
        return dp[0][n - 1]

        # @lru_cache(None)
        # def solution(lo, hi):
        #     if lo >= hi - 1:
        #         return 0
        #     coins = 0
        #     for i in range(lo + 1, hi):
        #         temp = nums[lo] * nums[i] * nums[hi]
        #         temp += solution(lo, i) + solution(i, hi)
        #         coins = max(coins, temp)
        #     return coins
        #
        # return solution(0, len(nums) - 1)


print(Solution().maxCoins(nums=[3, 1, 5, 8]))
