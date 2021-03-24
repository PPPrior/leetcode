""" Backtracking """
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(k, comb, cur=1):
            if k == 0:
                ans.append(comb)
                return
            for i in range(cur, n + 1):
                backtrack(k - 1, comb + [i], i + 1)

        ans = list()
        backtrack(k, [])
        return ans


print(Solution().combine(n=4, k=2))
