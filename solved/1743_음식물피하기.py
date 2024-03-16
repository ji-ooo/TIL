import sys
from collections import deque
input = sys.stdin.readline


N, M, K = map(int, input().split())

arr = [['.'] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    r -=1
    c -=1
    arr[r][c] = '#'

ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '#':
            tmp = 0
            que = deque([(i, j)])
            arr[i][j] = '.'

            while que:
                v = que.pop()
                x, y = v
                tmp += 1

                for dx, dy in ds:
                    nx, ny = x + dx, y +dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if arr[nx][ny] == '#':
                            arr[nx][ny] = '.'
                            que.append((nx, ny))

            result = max(result, tmp)
print(result)