""" Greedy """
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [float('-inf')] + nums + [float('inf')]
        n = 1
        for i in range(1, len(nums) - 2):
            if nums[i] > nums[i + 1]:
                n -= 1
                if n < 0:
                    return False
                if nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True


print(Solution().checkPossibility(nums=[3, 4, 2, 3]))
