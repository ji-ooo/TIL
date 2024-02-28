import sys
sys.stdin = open('1861.txt')

from collections import deque


def find_mx_mv(v):
    que = deque([v])
    cnt = 0
    while que:
        now = que.pop()
        x, y = now
        cnt += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == arr[x][y] + 1:
                    que.append((nx, ny))
    return cnt


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mv = [[0] * N for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            mv[i][j] = find_mx_mv((i, j))
            mx = max(mx, mv[i][j])

    result = N**2+1
    for i in range(N):
        for j in range(N):
            if mv[i][j] == mx:
                result = min(result, arr[i][j])

    print(f'#{tc} {result} {mx}')

# dr = ((1, 0), (0, 1), (-1, 0), (0, -1))
#
# for tc in range(int(input())):
#     N = int(input())
#     DP = [0] * (N ** 2 + 1)
#     for r in range(N):
#         for c, v in enumerate(map(int, input().split())):
#             DP[v] = (r, c)
#     print(DP)
#     min_v, max_l, cnt, v = 1, 1, 1, 1
#     for n in range(1, len(DP)):
#         i, j = DP[n]
#         for di, dj in dr:
#             if DP[n - 1] == (i + di, j + dj):
#                 cnt += 1
#                 if max_l < cnt:
#                     max_l, min_v = cnt, v
#                 break
#         else:
#             cnt, v = 1, n
#
#     print(f'#{tc + 1}', min_v, max_l)
