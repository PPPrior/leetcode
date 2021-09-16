from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        lo, hi = 0, len(people) - 1
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
            ans += 1
        return ans


print(Solution().numRescueBoats(people=[3, 2, 2, 1], limit=3))
