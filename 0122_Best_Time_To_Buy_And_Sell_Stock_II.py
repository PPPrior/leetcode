""" Greedy """
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(len(prices) - 1):
            k = prices[i + 1] - prices[i]
            p += k if k > 0 else 0
        return p


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
