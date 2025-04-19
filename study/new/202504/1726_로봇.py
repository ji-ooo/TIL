from collections import deque

M, N = map(int, input().split())

grid = []
for _ in range(M):
    grid.append(list(map(int, input().split())))

sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sx -= 1; sy -= 1
ex -= 1; ey -= 1

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

left = {1: 4, 2: 3, 3: 1, 4: 2}
right = {1: 3, 2: 4, 3: 2, 4: 1}

visited = [[[False for _ in range(5)] for _ in range(N+1)] for _ in range(M+1)]
que = deque([(sx, sy, sd, 0)])
visited[sx][sy][sd] = True

ans = 0
while que:
    x, y, dir, count = que.popleft()
    
    if x == ex and y == ey and dir == ed:
        ans = count
        break

    new_dir = left[dir]
    if not visited[x][y][new_dir]:
        que.append((x, y, new_dir, count + 1))
        visited[x][y][new_dir] = True
        
    new_dir = right[dir]
    if not visited[x][y][new_dir]:
        que.append((x, y, new_dir, count + 1))
        visited[x][y][new_dir] = True
    
    for k in range(1, 4):
        nx = x + dx[dir] * k
        ny = y + dy[dir] * k
        
        if 0 <= nx < M and 0 <= ny < N and not grid[nx][ny]:
            if not visited[nx][ny][dir]:
                que.append((nx, ny, dir, count + 1))
                visited[nx][ny][dir] = True
        else:
            break

print(ans)
