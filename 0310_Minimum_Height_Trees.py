"""  """
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0] * n
        connected = [[] for _ in range(n)]
        for v1, v2 in edges:
            degree[v1] += 1
            degree[v2] += 1
            connected[v1].append(v2)
            connected[v2].append(v1)

        queue = [i for i, v in enumerate(degree) if v == 1]
        ans = list()
        while queue:
            ans.clear()
            for _ in range(len(queue)):
                v = queue.pop(0)
                ans.append(v)
                adj = connected[v]
                for w in adj:
                    degree[w] -= 1
                    if degree[w] == 1:
                        queue.append(w)
        return ans if n > 1 else [0]


print(Solution().findMinHeightTrees(n=3, edges=[[0, 1], [0, 2]]))
