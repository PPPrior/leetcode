""" Stack """


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ""
        for ch in S:
            if stack and stack[-1] == ch:
                stack = stack[:-1]
            else:
                stack += ch
        return stack


print(Solution().removeDuplicates(S="abbaca"))
