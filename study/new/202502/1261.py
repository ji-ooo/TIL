import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(M)]

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]


visited = [[1e9] * N for _ in range(M)]
visited[0][0] = 0

stack = []
heappush(stack, (0, 0, 0))
while stack:
    b, x, y = heappop(stack)
    if x == M-1 and y == N-1:
        break

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if arr[nx][ny] == 1:
                if b + 1 < visited[nx][ny]:
                    heappush(stack, (b + 1, nx, ny))
                    visited[nx][ny] = b + 1
            else:
                if b < visited[nx][ny]:
                    heappush(stack, (b, nx, ny))
                    visited[nx][ny] = b
    
print(visited[M-1][N-1])