""" Backtracking """
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, tmp, target):
            if target == 0:
                ans.append(tmp)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                diff = target - nums[i]
                if diff < 0:
                    break
                backtrack(nums[i + 1:], tmp + [nums[i]], diff)

        ans = list()
        backtrack(sorted(candidates), [], target)
        return ans


print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
