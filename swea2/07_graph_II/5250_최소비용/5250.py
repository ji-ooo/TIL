import sys
sys.stdin = open('5250.txt')

from heapq import heappush, heappop


def dijk(start):
    pq = []
    distance = [[1e9] * N for _ in range(N)]
    distance[0][0] = 0

    heappush(pq, (0, start))
    while pq:
        dist, now = heappop(pq)
        x, y = now
        if distance[x][y] < dist:
            continue

        now_h = arr[x][y]

        for dx, dy in ds:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                nxt_h = arr[nx][ny]
                extra = 0
                if now_h < nxt_h:
                    extra = nxt_h - now_h
                nxt_dist = dist + extra + 1

                if distance[nx][ny] <= nxt_dist:
                    continue
                distance[nx][ny] = nxt_dist
                heappush(pq, (nxt_dist, (nx, ny)))

    print(f'#{tc} {distance[N - 1][N - 1]}')


ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dijk((0, 0))
