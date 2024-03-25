import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
link = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e, d = map(int, input().split())
    link[s] = [e, d]

for _ in range(M):
    S, E = map(int, input().split())
    que = deque([(S, 0)])
    visited = [0 for _ in range(N+1)]
    visited[S] = 1
    result = 0
    while que:
        x = que.popleft()
        v, d = x
        if link[v]:
            nxt, dist = link[v]
            dist += d
            if nxt == E:
                result = dist
                break
            
            if not visited[nxt]:
                que.append((nxt, dist))
                visited[nxt] = 1

        if result: break
    print(dist)
    
        