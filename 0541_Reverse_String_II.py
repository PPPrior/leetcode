""" Two Pointers """


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), k * 2):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)


print(Solution().reverseStr(s="abcdefg", k=2))
