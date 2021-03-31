""" Backtracking """
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp, count):
            if len(tmp) == count:
                ans.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[i + 1:], tmp + [nums[i]], count)

        ans = list()
        for i in range(len(nums) + 1):
            backtrack(nums, [], i)
        return ans


print(Solution().subsets(nums=[1, 2, 3]))
