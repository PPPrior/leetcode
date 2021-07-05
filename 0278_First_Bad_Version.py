# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    bad = 4
    return version >= bad


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo


print(Solution().firstBadVersion(n=5))
