""" Two Pointers """
from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def checkWord(s, word):
            j = 0
            for i, ch in enumerate(s):
                if ch == word[j]:
                    j += 1
                    if j == len(word):
                        return word
            return ''

        ans, n = '', 0
        for word in d:
            rst = checkWord(s, word)
            if len(rst) > n or (len(rst) == n and rst < ans):
                ans, n = rst, len(rst)
        return ans


print(Solution().findLongestWord(s="aba", d=["ba", "ab", "a", "b"]))
