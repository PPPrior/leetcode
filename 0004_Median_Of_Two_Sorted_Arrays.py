""" Binary Search """
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            i = j = 0
            while True:
                if i == m:
                    return nums2[j + k - 1]
                if j == n:
                    return nums1[i + k - 1]
                if k == 1:
                    return min(nums1[i], nums2[j])

                p1 = min(m - 1, i + k // 2 - 1)
                p2 = min(n - 1, j + k // 2 - 1)
                if nums1[p1] > nums2[p2]:
                    k -= p2 - j + 1
                    j = p2 + 1
                else:
                    k -= p1 - i + 1
                    i = p1 + 1

        m, n = len(nums1), len(nums2)
        t = m + n
        if (m + n) & 1:
            return getKthElement((t + 1) // 2)
        else:
            return (getKthElement(t // 2) + getKthElement(t // 2 + 1)) / 2


print(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
