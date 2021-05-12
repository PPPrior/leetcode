""" Bit Manipulation """
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp, ans = [0], []
        for num in arr:
            dp.append(dp[-1] ^ num)
        for i, j in queries:
            ans.append(dp[i] ^ dp[j + 1])
        return ans


print(Solution().xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))
