""" Stack """


class Solution:
    def calculate(self, s: str) -> int:
        stack, op, num, n = list(), '+', 0, len(s)
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if i == n - 1 or ch in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op, num = ch, 0
        return sum(stack)


print(Solution().calculate(s="3+2*2"))
