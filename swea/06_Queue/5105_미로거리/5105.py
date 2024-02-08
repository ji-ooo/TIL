import sys
sys.stdin = open('5105.txt')

from collections import deque


def bfs(que, visited):
    global dist
    global result
    dist += 1
    nxt_que = deque([])
    while que:
        v = que.pop()
        x, y = v
        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] is False:
                if arr[nx][ny] == 0:
                    nxt_que.append((nx, ny))
                elif arr[nx][ny] == 3:
                    result = dist-1
                    return

    if nxt_que:
        bfs(nxt_que, visited)
    return


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    start = (0, 0)
    for i in range(N):
        line = list(map(int, input()))
        for j in range(N):
            if line[j] == 2:
                start = (i, j)
        arr.append(line)

    que = deque([start])
    visited = [[False]*N for _ in range(N)]

    dist = 0
    result = 0
    bfs(que, visited)

    print(f'#{tc} {result}')
