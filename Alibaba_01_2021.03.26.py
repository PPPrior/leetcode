"""
Alibaba 01 (2021.03.26)
Refer to <LeetCode No.1493>

input:
2
3
1 1 1
6
1 1 0 1 0 1

output:
2
3
"""


def solution(n, nums):
    ans = 0
    i, c = 0, 0
    for j in range(n):
        if nums[j] == '0':
            c += 1
        while c > 1:
            if nums[i] == '0':
                c -= 1
            i += 1
        ans = max(ans, j - i)
    print(ans)


def main():
    c = int(input())
    for i in range(c):
        n = int(input())
        nums = input().split(' ')
        solution(n, nums)


if __name__ == '__main__':
    main()
