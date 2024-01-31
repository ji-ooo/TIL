import sys
sys.stdin = open('1979.txt')

def search_x(x, y):
    for i in range(K):
        if arr[x + i][y] != 1:
            return 0
    if x + K < N:
        if arr[x + K][y] == 1:
            return 0

    return 1


def search_y(x, y):
    for i in range(K):
        if arr[x][y + i] != 1:
            return 0
    if y + K < N:
        if arr[x][y + K] == 1:
            return 0

    return 1


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        line = list(map(int, input().split()))
        arr.append(line)

    ans = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                if x == 0:
                    ans += search_x(x, y)
                elif arr[x - 1][y] == 0 and x + K - 1 < N:
                    ans += search_x(x, y)

                if y == 0:
                    ans += search_y(x, y)
                elif arr[x][y - 1] == 0 and y + K - 1 < N:
                    ans += search_y(x, y)

    print(f'#{tc} {ans}')
