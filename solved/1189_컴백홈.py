from collections import deque

def bfs(v, dist):
    global result
    # print(v, dist)
    if dist == K and v == end:
        result += 1
        return
    elif dist == K:
        return
    
    x, y = v
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < R and 0 <= ny < C:
            if arr[nx][ny] == '.':
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    bfs((nx, ny), dist + 1)
                    visited[nx][ny] = 0
                    
                


R, C, K = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]

start = (R-1, 0)
end = (0, C-1)

visited = [[0] * C for _ in range(R)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

result = 0
visited[R-1][0] = 1
bfs(start, 1)
print(result)


