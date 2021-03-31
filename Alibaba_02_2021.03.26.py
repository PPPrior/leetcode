"""
Alibaba 02 (2021.03.26)
Refer to <LeetCode No.1493>

input:  n个酒店,n-1条道路,3个人
4       n个酒店,n-1条道路
1 2 3   道路1 (u,v,w) u酒店到v酒店的距离w
4 3 9   ...
3 1 6   道路n-1
2 1 4   同学1 (n,v1...vn) 期望入住v1...vn共n个酒店
1 2     同学2
1 3     同学3

output:
13.5    期望路径
        入住1,2,3 最短路径9
        入住4,2,3 最短路径18
"""


def solution(n, path, pref):
    for i in range(n):
        for j in range(i + 1, n):
            path[j][i] = path[i][j] = min([path[i][k] + path[k][j] for k in range(n)])
    ans = []
    for x, y, z in pref:
        ans.append(min([path[i][x] + path[i][y] + path[i][z] for i in range(n)]))
    print(sum(ans) / len(ans))


def main():
    n = int(input())
    path = [[float('inf')] * n for _ in range(n)]
    pref = []
    for i in range(n):
        path[i][i] = 0
    for i in range(n - 1):
        u, v, w = [int(x) for x in input().split()]
        path[u - 1][v - 1] = path[v - 1][u - 1] = w
    for i in range(3):
        pref.append([int(x) - 1 for x in input().split()][1:])
    pref = [[x, y, z] for x in pref[0] for y in pref[1] for z in pref[2]]

    solution(n, path, pref)


if __name__ == '__main__':
    main()
