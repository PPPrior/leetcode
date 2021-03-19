""" Backtracking """
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # DFS
        def backtrace(combination, digits):
            if digits:
                for letter in phone[digits[0]]:
                    backtrace(combination + letter, digits[1:])
            else:
                ans.append(combination)

        ans = []
        backtrace('', digits)
        return ans

    """ List Comprehension """
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = ['']
        for n in digits:
            ans = [p + q for p in ans for q in phone[n]]
        return ans
    """


print(Solution().letterCombinations(digits="29"))
