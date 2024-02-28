import sys
sys.stdin = open('5188.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if (i, j) == (0, 0):
                continue

            if i == 0:
                arr[i][j] += arr[i][j-1]
            elif j == 0:
                arr[i][j] += arr[i-1][j]
            else:
                arr[i][j] += min(arr[i-1][j], arr[i][j-1])
    print(f'#{tc} {arr[N - 1][N - 1]}')