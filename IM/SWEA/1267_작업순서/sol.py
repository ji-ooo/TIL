import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split())
    line = deque(list(map(int, input().split())))
    link = {i:[] for i in range(V+1)}
    e_list = [1 for _ in range(V+1)]
    for _ in range(E):
        s, e = line.popleft(), line.popleft()
        link[s].append(e)
        e_list[e] -= 1

    que = deque([])
    for i in range(1, V+1):
        if e_list[i] == 1:
            que.append(i)

    visited = [False] * (V+1)
    arr = []
    while que:
        v = que.popleft()
        visited[v] = True
        arr.append(v)
        for nxt in link[v]:
            if not visited[nxt]:
                que.append(nxt)
                
    print(arr)


