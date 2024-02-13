import sys
sys.stdin = open('1227.txt')

from collections import deque

T = 10
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for t in range(1, T+1):
    tc = int(input())
    arr = []
    start = (1, 1)
    result = 0
    for i in range(100):
        line = list(map(int, input()))
        arr.append(line)

    visited = [[False] * 100 for _ in range(100)]
    que = deque([start])
    while que:
        v = que.pop()
        x, y = v
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 100 and 0 <= ny < 100:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                if arr[nx][ny] == 3:
                    result = 1
                    break

        if result:
            break
    print(f'#{tc} {result}')