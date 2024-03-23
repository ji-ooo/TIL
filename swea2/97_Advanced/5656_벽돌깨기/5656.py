import sys
sys.stdin = open('5656.txt')
from collections import deque

ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def backtrack(cnt, arr):
    global result
    if cnt == N:
        tmp_cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    tmp_cnt += 1

        if result > tmp_cnt:
            result = tmp_cnt
        return

    for col in range(W):
        new_arr = [line[:] for line in arr]
        row = 0

        while row < H and not new_arr[row][col]:
            row += 1

        if row != H:
            brekin(row, col, new_arr)
            grav(new_arr)
            flag = brkinpoint(new_arr)

            if flag:
                backtrack(cnt+1, new_arr)
            else:
                backtrack(N, new_arr)


def brekin(x, y, arr):
    que = deque([(x, y)])

    visited = [[0] * W for _ in range(H)]
    visited[x][y] = 1
    while que:
        x, y = que.pop()
        splash = arr[x][y]
        arr[x][y] = 0

        if splash <= 1:
            continue

        for dx, dy in ds:
            for j in range(1, splash):
                nx = x + dx * j
                ny = y + dy * j
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        que.append((nx, ny))


def grav(arr):
    for i in range(W):
        brick = []
        for j in range(H):
            if arr[j][i]:
                brick.append(arr[j][i])
            arr[j][i] = 0

        for j in range(len(brick)):
            arr[H - 1 - j][i] = brick.pop()


def brkinpoint(arr):
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                return True
    return False


for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    result = W * H
    backtrack(0, arr)

    print(f'#{tc} {result}')

# def mk_link(v, k):
#     x, y = v
#
#     for i in range(-k+1, k):
#         for j in range(-k+1, k):
#             nx, ny = x+i, y+j
#             if 0 <= nx < H and 0 <= ny < W:
#                 pass
#
# for tc in range(1, int(input())+1):
#     N, W, H = map(int, input().split())
#     arr = []
#     cnt = 0
#     for _ in range(H):
#         line = list(map(int, input().split()))
#         for x in line:
#             if line:
#                 cnt += 1
#         arr.append(line)
#
#     dic = {}
#     for i in range(H):
#         for j in range(W):
#             if arr[i][j] > 1:
#                 mk_link((i, j), arr[i][j])
#
#
#     result = 0
#
#
#     '''
#     완탐 절대안댐
#     그냥 링크하는게 맞을듯
#     1보다 클때, 다음에 터트릴 수 있는 애들을 링크
#     각 좌표를 key로, 해시 하나 만들어서
#     다음 터지는 좌표 싹다 리스트로 value에 넣기
#
#     한번 터트릴때마다 링크를 갱신?
#     그럼 다른 케이스 조사는 어떻게함
#
#     12개만 딱 조사해서 링크 넣는거는
#     그럼 한번 할때마다 12개씩 링크 연결 할 수 있지않을까
#     '''
#