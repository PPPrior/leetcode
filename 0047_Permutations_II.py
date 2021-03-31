""" Backtracking """
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp):
            if not nums:
                ans.append(tmp)
                return
            k = len(nums)
            for i in range(k):
                if 0 < i and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        ans = list()
        nums.sort()
        backtrack(nums, [])
        return ans


print(Solution().permuteUnique(nums=[1, 1, 2]))
