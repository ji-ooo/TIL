from collections import deque

# 대각선 까지 탐색 해야함
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# 세러 올때마다 갯수 카운트 하는게 편할 거 같아서 함수 만들엇음
def dfs(i, j):
    # 방문한거는 global
    global visited
    que = deque([(i, j)])
    # pop해서 탐색햇으니까 깊이 우선인데
    # popleft해서 탐색해도 똑같이 나올 거 같음
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
    # 방문처리 배열
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