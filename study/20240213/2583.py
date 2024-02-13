from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i, j):
    sq = 0
    que = deque([(i, j)])
    while que:
        sq += 1
        v = que.pop()
        x, y = v
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    
    return sq

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    ax, ay, bx, by = map(int, input().split())

    for i in range(ay, by):
        for j in range(ax, bx):
            arr[i][j] = 1

sq_lst = []
cnt = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            sq_lst.append(dfs(i, j))
            cnt += 1

sq_lst.sort()
print(cnt)
print(*sq_lst)