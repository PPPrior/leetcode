""" Array """
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]
        t = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * t
            t *= nums[i]
        return ans


print(Solution().productExceptSelf(nums=[4, 3, 2, 1]))
