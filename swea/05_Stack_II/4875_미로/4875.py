import sys
sys.stdin = open('4875.txt')

from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                current = (i, j)
                break

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = [[False] * N for _ in range(N)]
    que = deque([current])

    flag = False
    while que:
        current = que.pop()
        x, y = current
        visited.append(current)

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    arr[nx][ny] = 2
                elif arr[nx][ny] == 3:
                    flag = True
                    break

        if flag:
            break
    if flag:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')

