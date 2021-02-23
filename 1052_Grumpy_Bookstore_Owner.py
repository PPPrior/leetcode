""" Sliding Window """
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n, m = 0, 0
        for i in range(X):
            n += 0 if grumpy[i] else customers[i]
            m += customers[i] if grumpy[i] else 0
        w = m
        for i in range(X, len(customers)):
            n += 0 if grumpy[i] else customers[i]
            w += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            m = max(w, m)
        return n + m


print(Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3))
