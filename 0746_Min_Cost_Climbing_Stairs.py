""" Dynamic Programming """
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i]=min(dp[i-1]+cost[i],dp[i-2]+cost[i])
        cost = [0] + cost + [0]
        n, p, q = len(cost), cost[1], cost[2]
        for i in range(3, n):
            p, q = q, min(p + cost[i], q + cost[i])
        return q


print(Solution().minCostClimbingStairs(cost=[10, 15, 20]))
