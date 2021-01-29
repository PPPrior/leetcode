""" Two Pointers """
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            n = numbers[i] + numbers[j]
            if n == target:
                return [i + 1, j + 1]
            elif n < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]


print(Solution().twoSum(numbers=[0, 0, 3, 4], target=0))
