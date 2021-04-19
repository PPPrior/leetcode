""" Dynamic Programming """
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        price, cd_profit, profit = float('inf'), 0, 0
        for i in range(n):
            new_price = min(price, prices[i] - profit)
            new_cd_profit = prices[i] - price
            new_profit = max(cd_profit, profit)
            price, cd_profit, profit = new_price, new_cd_profit, new_profit
        return max(cd_profit, profit)


print(Solution().maxProfit(prices=[1, 2, 3, 0, 2]))
