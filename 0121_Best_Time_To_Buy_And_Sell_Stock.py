""" Dynamic Programming """
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
