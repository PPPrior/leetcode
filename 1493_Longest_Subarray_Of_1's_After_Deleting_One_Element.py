""" Sliding Window """
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n, i, c = len(nums), 0, 0
        ans = 0
        for j in range(n):
            if nums[j] == 0:
                c += 1
            while c > 1:
                if nums[i] == 0:
                    c -= 1
                i += 1
            ans = max(ans, j - i)
        return ans


print(Solution().longestSubarray(nums=[1, 0, 1, 1, 1]))
