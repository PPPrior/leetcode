""" Two Pointers """


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validSubPalindrome(p1, p2):
            while p1 < p2:
                if s[p1] != s[p2]:
                    return False
                p1 += 1
                p2 -= 1
            return True

        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return validSubPalindrome(p1 + 1, p2) or validSubPalindrome(p1, p2 - 1)
        return True


print(Solution().validPalindrome(s="abca"))
