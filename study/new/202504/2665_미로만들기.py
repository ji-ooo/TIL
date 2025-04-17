import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
for _ in range(n):
    l = input().rstrip()
    line = []
    for i in l:
        line.append(int(i))
    arr.append(line)

visited = [[1e9 for _ in range(n)] for _ in range(n)]
dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

que = deque([(0, 0)])
visited[0][0] = 0

while que:
    x, y = que.popleft()
    
    if x == n-1 and y == n-1:
        break

    now = visited[x][y]

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            nxt = visited[nx][ny]

            if now >= nxt:
                continue

            if not arr[nx][ny]:
                if visited[nx][ny] > now + 1:
                    visited[nx][ny] = now + 1
                    que.append((nx, ny))

            else:
                visited[nx][ny] = now
                que.appendleft((nx, ny))

print(visited[n-1][n-1])
