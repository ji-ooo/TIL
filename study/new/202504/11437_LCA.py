import sys
from collections import deque
input = sys.stdin.readline


def sol(v, w):
    if dep[v] < dep[w]:
        v, w = w, v

    while dep[v] != dep[w]:
        v = par[v]

    while v != w:
        v = par[v]
        w = par[w]

    return v


N = int(input())
par = [0] * (N+1)
dep = [0] * (N+1)
visited = [False] * (N+1)
link = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

que = deque([1])
visited[1] = True
while que:
    v = que.popleft()

    for n in link[v]:
        if visited[n]:
            continue
        
        visited[n] = True
        dep[n] = dep[v] + 1
        par[n] = v
        que.append(n)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    print(sol(a, b))