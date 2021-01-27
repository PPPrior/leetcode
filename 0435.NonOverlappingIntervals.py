""" Greedy """
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n, m = 0, float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] >= m:
                m = intervals[i][1]
                n += 1
        return len(intervals) - n


print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]))
