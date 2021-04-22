""" Divide and Conquer """
from typing import List


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1: [1]}

        def solution(n):
            if n not in memo:
                odd = solution((n + 1) // 2)
                even = solution(n // 2)
                memo[n] = [x * 2 - 1 for x in odd] + [x * 2 for x in even]
            return memo[n]

        return solution(N)


print(Solution().beautifulArray(N=5))
