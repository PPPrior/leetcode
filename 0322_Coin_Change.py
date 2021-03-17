""" Dynamic Programming """
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            temp = [dp[i - n] for n in coins if i >= n and dp[i - n] >= 0]
            dp[i] = 1 + min(temp) if temp else -1
        return dp[amount]


print(Solution().coinChange(coins=[2], amount=3))
