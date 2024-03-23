import sys
input = sys.stdin.readline
from collections import deque


def Wbfs(v):
    x, y = v
    visited[x][y] = 1
    que = deque([v])
    
    cnt = 1
    while que:
        x, y = que.popleft()
        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 'W' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cnt += 1
                    que.append((nx, ny))
        
    return cnt**2

def Bbfs(v):
    x, y = v
    visited[x][y] = 1
    que = deque([v])
    
    cnt = 1
    while que:
        x, y = que.popleft()
        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 'B' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cnt += 1
                    que.append((nx, ny))
        
    return cnt**2


N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

result = [0, 0]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if arr[i][j] == 'W':
                result[0] += Wbfs((i, j))
            else:
                result[1] += Bbfs((i, j))

print(*result)