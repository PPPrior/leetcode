""" Two Pointers """
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write, anchor = 0, 0
        for read, ch in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != ch:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for n in str(read - anchor + 1):
                        chars[write] = n
                        write += 1
                anchor = read + 1
        return write


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
