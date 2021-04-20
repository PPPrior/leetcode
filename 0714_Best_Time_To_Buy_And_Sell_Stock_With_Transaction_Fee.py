""" Dynamic Programming """
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        min_price, max_profit = float('inf'), 0
        for i in range(n):
            min_price = min(min_price, prices[i] - max_profit)
            max_profit = max(max_profit, prices[i] - min_price - fee)
        return max_profit


print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
