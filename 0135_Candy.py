""" Greedy """
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        m = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                m[i] = m[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                m[i] = max(m[i], m[i + 1] + 1)
        return sum(m)


print(Solution().candy(ratings=[1, 3, 4, 5, 2]))
