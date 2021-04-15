""" Dynamic Programming """
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if n <= k:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        max_profit, min_price = [0] * (k + 1), [float('inf')] * (k + 1)
        for i in range(n):
            for j in range(1, k + 1):
                min_price[j] = min(min_price[j], prices[i] - max_profit[j - 1])
                max_profit[j] = max(max_profit[j], prices[i] - int(min_price[j]))
        return max_profit[k]


print(Solution().maxProfit(k=2, prices=[3, 3, 5, 0, 0, 3, 1, 4]))
