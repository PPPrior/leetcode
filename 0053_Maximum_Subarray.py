""" Dynamic Programming """
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, ans = 0, nums[0]
        for num in nums:
            sum = sum + num if sum > 0 else num
            ans = max(ans, sum)
        return ans
        
    """
    def maxSubArray(self, nums: List[int]) -> int:
        n, ans = len(nums), float('-inf')
        dp = [0] * n
        for i in range(n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(dp[i], ans)
        return ans
    """


print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
