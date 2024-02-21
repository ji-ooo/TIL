from collections import deque
from pprint import pprint as print

N, M = map(int, input().split())
arr = []
for _ in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def melt(v, arr, visited):
    global cnt

    que = deque([v])
    
    while que:
        m = 0
        x, y = que.popleft()
        visited[x][y] = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = 1
            if arr[nx][ny] == 0 and not visited[nx][ny]:
                m += 1
        arr[x][y] -= m

        if arr[x][y] < 0:
            arr[x][y] = 0
    print(arr)
    print(cnt)
    print(result)
    print('---')

result = 0
while True:
    visited = [[0] * M for _ in range(N)]
    result += 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                melt((i, j), arr, visited)
                cnt += 1
    if cnt >2:
        break
    elif cnt == 0:
        break            
    

print(result)