import sys
from collections import deque
input = sys.stdin.readline

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

r, c = map(int, input().split())
miro = []
fire = []
visited = [[0] * c for _ in range(r)]

for i in range(r):
    line = list(input().strip())
    for j in range(c):
        t = line[j]
        
        if t == 'J':
            pos = (x, y) = (i, j)
            
        elif t == 'F':
            fire.append((i, j))
            visited[i][j] = 1

    miro.append(line)

que = deque(fire)

while que:
    x, y = que.popleft()
    t = visited[x][y]

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if miro[nx][ny] in ('.', 'J') and not visited[nx][ny]:
                visited[nx][ny] = t + 1
                que.append((nx, ny))

x, y = pos
visited[x][y] = 1
que.append(pos)

ans = 0
while que:
    x, y = que.popleft()
    t = visited[x][y]

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if miro[nx][ny] == '.':
                if not visited[nx][ny] or t + 1 < visited[nx][ny]:
                    visited[nx][ny] = t + 1
                    que.append((nx, ny))
        else:
            ans = t
            que = []
            break

print(ans if ans != 0 else 'IMPOSSIBLE')
    