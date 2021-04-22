""" Divide and Conquer """
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i, ch in enumerate(expression):
            if ch in ["+", "-", "*"]:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for num1 in left:
                    for num2 in right:
                        if ch == "+":
                            ans.append(num1 + num2)
                        elif ch == "-":
                            ans.append(num1 - num2)
                        else:
                            ans.append(num1 * num2)
        return ans


print(Solution().diffWaysToCompute("2*3-4*5"))
