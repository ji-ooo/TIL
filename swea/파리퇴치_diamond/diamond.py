import sys
sys.stdin = open('input.txt')


def fly(v, M):
    x, y = v
    m = M//2
    s = 0
    tmp = 0
    for i in range(-m, m+1):
        for j in range(-m, m+1):
            if abs(i) + abs(j) <= m:
                nx, ny = x + i, y + j
                if 0 <= nx < N and 0 <= ny < N:
                    tmp += arr[nx][ny]
            s = max(s, tmp)
    return s


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            result = max(fly((i, j), M), result)

    print(result)