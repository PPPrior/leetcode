""" Breadth-first Search """
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = [(i, 1 << i, 0) for i in range(n)]
        visited = {(i, 1 << i) for i in range(n)}
        ans = 0
        while queue:
            u, mask, dist = queue.pop(0)
            if mask == (1 << n) - 1:
                ans = dist
                break
            for v in graph[u]:
                mask_v = mask | (1 << v)
                if (v, mask_v) not in visited:
                    visited.add((v, mask_v))
                    queue.append((v, mask_v, dist + 1))
        return ans


print(Solution().shortestPathLength(graph=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
