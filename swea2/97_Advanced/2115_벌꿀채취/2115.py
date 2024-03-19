import sys
sys.stdin = open('2115.txt')


def honey(x, y, c, s):
    global result

    if c == 2:
        result = max(result, s)
        return

    else:
        for k in range(M):
            s += arr[x][y+k]**2

        for i in range(x, N):
            tmp = 0
            if i == x:
                for j in range(y+M, N-M):
                    for k in range(M):
                        tmp += arr[i][j]
                    if tmp <= C:
                        honey(i, j, c+1, s)
                    else:
                        return
            else:
                for j in range(N-M):
                    for k in range(M):
                        tmp += arr[i][j]
                    if tmp <= C:
                        honey(i, j, c + 1, s)
                    else:
                        return


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N-M):
            tmp = 0
            for k in range(M):
                tmp += arr[i][j+k]
            if tmp <= C:
                honey(i, j, 0, 0)
    print(result)