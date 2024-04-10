import sys
sys.stdin = open('4014.txt')

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def check(v, d):
    global col, row
    x, y = v
    dx, dy, f = d
    now = arr[x][y]
    if f:
        if y + dy*X < 0 or y + dy*X >= N:
            row[x] = 0
            return
        for k in range(1, X+1):
            if used[x][y + k * dy][0]:
                row[x] = 0
                return

            used[x][y + k * dy][0] = 1

            if arr[x][y + k * dy] == now-1:
                continue
            else:
                row[x] = 0
                return


    else:
        if x + dx*X < 0 or x + dx*X >= N:
            col[y] = 0
            return

        for k in range(1, X+1):
            if used[x + k * dx][y][1]:
                col[y] = 0
                return

            used[x + k * dx][y][1] = 1

            if arr[x + k * dx][y] == now-1:
                continue
            else:
                col[y] = 0
                return


for tc in range(1, int(input())+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mn_h = 0

    used = [[[0, 0] for _ in range(N)] for _ in range(N)]
    row = [1] * N
    col = [1] * N

    for h in range(N):
        mn_h = min(mn_h, min(arr[h]))

    for i in range(N):
        for j in range(N):
            for di, dj in dr:
                if di and not col[j]:
                    continue
                elif dj and not row[i]:
                    continue

                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[i][j] > arr[ni][nj]:
                        if di:
                            check((i, j), (di, dj, 0))
                        elif dj:
                            check((i, j), (di, dj, 1))
    # print(row, col)
    result = N * 2
    for t in range(N):
        if not row[t]:
            result -= 1
        if not col[t]:
            result -= 1

    print(f'#{tc} {result}')


    '''
    2차원 배열 탐색 하면서
    가장 낮은 칸이면 continue
    가장 낮은 칸이 아닐 때 탐색하는게 맞는듯

    2차원 탐색한 좌표에서 dr 4방향에 따라 함수실행
    현재 좌표 +- X 해서 범위 벗어나는지 판단 먼저
    범위보다 작으면 (i, j), d 넣어서 탐색
    함수 실행 시 받은 d 인자를 계속 재귀로 주기
    
    다 되는거로 해놓고, 안되면 빼주면 될듯 ?
    그러면 다 같은높이 인 경우 따로 체크 안해도 됨
    '''