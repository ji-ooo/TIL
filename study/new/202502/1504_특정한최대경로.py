import sys
input = sys.stdin.readline

from heapq import heappop, heappush


def dijk(n1, n2):
    if n1 == n2:
        return 0
    
    visited = [1e9] * (N+1)
    que = []
    heappush(que, (0, n1))

    while que:
        now_dist, now = heappop(que)
        
        if now_dist > visited[now]:
            continue

        for nxt_dist, nxt in edge[now]:
            new_dist = now_dist + nxt_dist

            if visited[nxt] > new_dist:
                visited[nxt] = new_dist
                heappush(que, (new_dist, nxt))

    return visited[n2]


N, E = map(int, input().split())
edge = {i: [] for i in range(1, N+1)}

for _ in range(E):
    a, b, c = map(int, input().split())

    edge[a].append((c, b))
    edge[b].append((c, a))

v1, v2 = map(int, input().split())

Otov1 = dijk(1, v1)
Ntov1 = dijk(N, v1)

v2toN = dijk(v2, N)
v2toO = dijk(v2, 1)

mid = dijk(v1, v2)

ans = min(Otov1 + v2toN + mid,
          Ntov1 + v2toO + mid,
          Otov1 + Ntov1 + mid * 2,
          v2toO + v2toN + mid * 2)

if ans >= 1e9:
    exit(print(-1))

print(ans)
'''
1 v1 v2 N
N v1 v2 1
1 v1 v2 v1 N
1 v2 v1 v2 N
'''