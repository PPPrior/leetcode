""" Stack """


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False
        d = {'(': ')', '[': ']', '{': '}'}
        stack = list()
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if not stack or c != d[stack.pop()]:
                    return False
        return not stack


print(Solution().isValid(s="(("))
