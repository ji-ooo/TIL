from collections import deque


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            que = deque([(i, j)])
            visited[i][j] = 1
            while que:
                x, y = que.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] and not visited[nx][ny]:
                            que.append((nx, ny))
                            visited[nx][ny] = 1
