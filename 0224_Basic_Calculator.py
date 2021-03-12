""" Stack """


class Solution:
    def calculate(self, s: str) -> int:
        stack, num, ans, op = list(), 0, 0, 1
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in "+-":
                ans += op * num
                num = 0
                op = 1 if ch == "+" else -1
            if ch == "(":
                stack.append(ans)
                stack.append(op)
                ans, op = 0, 1
            if ch == ")":
                ans += op * num
                num = 0
                ans *= stack.pop()
                ans += stack.pop()
        ans += op * num
        return ans


print(Solution().calculate(s="(1+(4+5+2)-3)+(6+8)"))
