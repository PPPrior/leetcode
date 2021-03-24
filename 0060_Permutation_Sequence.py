""" Math """


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        dp = [1] * n
        for i in range(1, n):
            dp[i] = dp[i - 1] * i
        ans = ""
        while n:
            ans += str(nums.pop((k - 1) // dp[n - 1]))
            k %= dp[n - 1]
            n -= 1
        return ans


print(Solution().getPermutation(n=3, k=3))
