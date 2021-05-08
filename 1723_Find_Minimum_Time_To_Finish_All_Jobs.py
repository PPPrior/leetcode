""" Backtracking """
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtrack(jobs, alloc, limit):
            if not jobs:
                return True
            t = jobs.pop()
            for i in range(k):
                if alloc[i] + t > limit:
                    continue
                alloc[i] += t
                if backtrack(jobs, alloc, limit):
                    return True
                alloc[i] -= t
                if alloc[i] == 0:
                    break
            jobs.append(t)
            return False

        jobs.sort()
        lo, hi = jobs[-1], sum(jobs)
        while lo < hi:
            mid = (lo + hi) // 2
            if backtrack(jobs[:], [0] * k, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


print(Solution().minimumTimeRequired(jobs=[1, 2, 4, 7, 8], k=2))
