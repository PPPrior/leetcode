""" Dynamic Programming """
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0]
        for num in nums:
            self.preSum.append(self.preSum[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.preSum[j + 1] - self.preSum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
