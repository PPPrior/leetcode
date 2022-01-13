""" Backtracking """
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def backtrack(arr, temp):
            if not arr:
                ans.append(temp)
            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                backtrack(arr[:i] + arr[i + 1:], temp + arr[i])

        ans = []
        s = list(s)
        s.sort()
        backtrack(s, '')
        return ans


print(Solution().permutation(s="abc"))
