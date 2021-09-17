""" Dynamic Programming """
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int):
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                width = sum(x[0] for x in books[j - 1:i])
                if width > shelf_width:
                    break
                else:
                    height = max(x[1] for x in books[j - 1:i])
                    dp[i] = min(dp[i], dp[j - 1] + height)
        return dp[-1]


print(Solution().minHeightShelves(books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelf_width=4))
