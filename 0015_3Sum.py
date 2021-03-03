""" Two Pointers """
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n = list(), len(nums)
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                return ans
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                p1, p2 = i + 1, n - 1
                while p1 < p2:
                    sum = nums[p1] + nums[p2] + num
                    if sum > 0:
                        p2 -= 1
                    elif sum < 0:
                        p1 += 1
                    else:
                        ans.append([num, nums[p1], nums[p2]])
                        while p1 < p2 and nums[p1] == nums[p1 + 1]:
                            p1 += 1
                        while p1 < p2 and nums[p2] == nums[p2 - 1]:
                            p2 -= 1
                        p1 += 1
                        p2 -= 1
        return ans


print(Solution().threeSum(nums=[0, 0, 0, 0]))
