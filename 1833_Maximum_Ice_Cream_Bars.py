""" Greedy """
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for n in costs:
            if coins >= n:
                coins -= n
                ans += 1
            else:
                break
        return ans


print(Solution().maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))
