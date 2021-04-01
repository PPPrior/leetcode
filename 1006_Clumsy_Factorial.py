""" Stack """


class Solution:
    def clumsy(self, N: int) -> int:
        op, stack = 0, [N]
        N -= 1
        while N > 0:
            op %= 4
            if op == 0:
                stack.append(stack.pop() * N)
            elif op == 1:
                stack.append(int(stack.pop() / N))
            elif op == 2:
                stack.append(N)
            else:
                stack.append(-N)
            op += 1
            N -= 1
        return sum(stack)


print(Solution().clumsy(N=10))
