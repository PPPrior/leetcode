""" Backtracking """
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list()

        def backtrack(nums, tmp):
            if not nums:
                ans.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return ans


print(Solution().permute(nums=[1, 2, 3]))
