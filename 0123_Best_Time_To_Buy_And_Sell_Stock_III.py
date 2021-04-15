""" Dynamic Programming """
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit1, max_profit2 = 0, 0
        min_price1, min_price2 = float('inf'), float('inf')
        for price in prices:
            min_price1 = min(min_price1, price)
            max_profit1 = max(max_profit1, price - min_price1)
            min_price2 = min(min_price2, price - max_profit1)
            max_profit2 = max(max_profit2, price - min_price2)
        return max_profit2


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
