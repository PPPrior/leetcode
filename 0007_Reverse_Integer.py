class Solution:
    def reverse(self, x: int) -> int:
        def reverse(x):
            if x < 0:
                return -reverse(-x)
            y = 0
            while x != 0:
                y = y * 10 + x % 10
                x = x // 10
            return 0 if y > 2147483647 else y

        return reverse(x)


print(Solution().reverse(x=-120))
