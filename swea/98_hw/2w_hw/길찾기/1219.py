import sys
sys.stdin = open('1219.txt')

from collections import deque

for tc in range(1, 11):
    T, N = map(int, input().split())
    line = deque(list(map(int, input().split())))

    road = {i:[] for i in range(100)}
    for _ in range(N):
        x, y = line.popleft(), line.popleft()
        road[x].append(y)

    visited = []
    que = deque([0])
    while que:
        v = que.pop()
        visited.append(v)

        for i in road[v]:
            if i not in visited:
                que.append(i)

    if 99 in visited:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
