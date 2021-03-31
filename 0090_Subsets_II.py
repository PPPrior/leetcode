""" Backtracking """
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp, count):
            if len(tmp) == count:
                ans.append(tmp)
            else:
                k, i = len(nums), 0
                while i < k:
                    backtrack(nums[i + 1:], tmp + [nums[i]], count)
                    i += 1
                    while 0 < i < k and nums[i] == nums[i - 1]:
                        i += 1

        nums.sort()
        n, ans = len(nums), list()
        for i in range(n + 1):
            backtrack(nums, [], i)
        return ans


print(Solution().subsetsWithDup(nums=[4, 4, 4, 1, 4]))
