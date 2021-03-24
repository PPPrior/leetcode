""" Stack """
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n, t = len(nums), float('-inf')
        stack = list()
        for i in range(n - 1, -1, -1):
            if nums[i] < t:
                return True
            while stack and nums[i] > stack[-1]:
                t = stack.pop()
            stack.append(nums[i])
        return False


print(Solution().find132pattern(nums=[3, 5, 0, 3, 4]))
