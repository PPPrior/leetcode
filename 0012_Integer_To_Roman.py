""" Math """


class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
             50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        ans = ""
        for k, v in d.items():
            while num >= k:
                num -= k
                ans += v
        return ans


print(Solution().intToRoman(num=1994))
