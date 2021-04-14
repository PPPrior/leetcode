""" Backtracking """
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem:
            return False

        def backtrack():
            if not nums:
                return True
            num = nums.pop()
            for i in range(k):
                if buckets[i] == num or not nums or buckets[i] - num >= nums[0]:
                    buckets[i] -= num
                    if backtrack():
                        return True
                    buckets[i] += num
            nums.append(num)
            return False

        nums.sort()
        buckets = [target] * k
        return backtrack()


print(Solution().canPartitionKSubsets(nums=[10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], k=3))
