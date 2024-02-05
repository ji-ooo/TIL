import sys
sys.stdin = open('4871.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    link = {i: [] for i in range(1, V+1)}
    for _ in range(E):
        x, y = map(int, input().split())
        link[x].append(y)

    S, G = map(int, input().split())

    visited = []
    que = deque([S])

    while que:
        current = que.pop()
        visited.append(current)
        nxt = link[current]

        for i in range(len(nxt)):
            que.append(nxt[i])

    if G in visited:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
