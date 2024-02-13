from collections import deque


directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(i, j):
    global visited
    que = deque([(i, j)])
    while que:
        v = que.pop()
        x, y = v
        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    que.append((nx, ny))
    

w, h = map(int, input().split())
while True:
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    
    que = deque([])
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)


    w, h = map(int, input().split())
    if w == h == 0:
        break