import sys
from collections import deque
input = sys.stdin.readline

tc = 1

while True:
    N = int(input())
    if N == 0:
        exit()

    arr = [list(map(int, input().split())) for _ in range(N)]

    start = (0, 1)

    dr = [(1, -1), (1, 0), (1, 1), (0, 1)]

    dist = [[1e9] * 3 for _ in range(N)]
    dist[0][1] = arr[0][1]

    que = deque([start])
    while que:
        x, y = que.popleft()
        now = dist[x][y]

        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < 3:
                if now + arr[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = now + arr[nx][ny]
                    que.append((nx, ny))

    print(f'{tc}. {dist[N-1][1]}')
    tc += 1
