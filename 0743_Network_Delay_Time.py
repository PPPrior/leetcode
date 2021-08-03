""" Shortest Path """
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[float('inf')] * n for _ in range(n)]
        for u, v, w in times:
            graph[u - 1][v - 1] = w

        dist = [float('inf')] * n
        dist[k - 1] = 0
        visited = [False] * n

        for _ in range(n):
            x = -1
            for y, u in enumerate(visited):
                if not u and (x == -1 or dist[x] > dist[y]):
                    x = y
            visited[x] = True
            for y, time in enumerate(graph[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1


print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
