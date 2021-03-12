""" Stack """


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = list()
        for ch in preorder.split(','):
            stack.append(ch)
            while len(stack) > 2 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(-2)
        return len(stack) == 1 and stack.pop() == '#'


print(Solution().isValidSerialization(preorder="9,3,4,#,#,1,#,#,2,#,6,#,#"))
