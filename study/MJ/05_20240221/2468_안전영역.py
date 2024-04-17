from collections import deque


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(v, h):
    global cnt
    cnt += 1
    que = deque([v])
    while que:
        x, y = que.pop()
        visited[x][y] = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] >= h and not visited[nx][ny]:
                    que.append((nx, ny))

N = int(input())
arr = []
maxi = 0
mini = 101
for _ in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    maxi = max(maxi, max(line))
    mini = min(mini, min(line))

result = 0
for h in range(mini, maxi +1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] >= h:
                dfs((i, j), h)
    result = max(cnt, result)
print(result)
