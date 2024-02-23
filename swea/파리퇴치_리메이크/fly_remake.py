import sys
sys.stdin = open('input.txt')

def fly(v, M):
    global result
    x, y = v
    tmp = 0
    for i in range(M):
        for j in range(M):
            nx, ny = x + i, y + j
            if nx < N and ny < N:
                tmp += arr[nx][ny]

    for k in range(M-2):
        for l in range(M-2):
            Xx, Yy = x + 1+ k, y + 1 + l
            if Xx < N and Yy < N:
                tmp -= arr[Xx][Yy]

    result = max(tmp, result)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            fly((i, j), M)
    print(f'#{tc} {result}')
