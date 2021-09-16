from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n, i = len(chalk), 0
        k %= sum(chalk)
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
        return i


print(Solution().chalkReplacer(chalk=[3, 4, 1, 2], k=25))
