""" Backtracking """
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, tmp, target):
            if target == 0:
                ans.append(tmp)
                return
            for i in range(len(nums)):
                diff = target - nums[i]
                if diff < 0:
                    break
                backtrack(nums[i:], tmp + [nums[i]], diff)

        ans = list()
        candidates.sort()
        backtrack(candidates, [], target)
        return ans


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
