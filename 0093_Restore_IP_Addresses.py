""" Backtracking """
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, n, tmp):
            if n == 0 and not s:
                ans.append('.'.join(tmp))
                return
            for i in range(1, 1 + min(3, len(s))):
                addr, remain = s[:i], s[i:]
                if len(remain) > (n - 1) * 3:
                    continue
                if int(addr) > 255 or (len(addr) > 1 and addr[0] == '0'):
                    continue
                backtrack(s[i:], n - 1, tmp + [s[:i]])

        ans = []
        backtrack(s, 4, [])
        return ans


print(Solution().restoreIpAddresses(s="010010"))
