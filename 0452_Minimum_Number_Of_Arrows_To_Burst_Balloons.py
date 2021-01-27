""" Greedy """
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        n, m = 0, float('-inf')
        for i in range(len(points)):
            if points[i][0] > m:
                m = points[i][1]
                n += 1
        return n


print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
