import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

inf = float('inf')

dist = [inf] * (N + 1)
dist[1] = 0

ans = 0
for _ in range(N-1):
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
        
for u, v, w in edges:
    if dist[u] + w < dist[v]:
        exit(print(-1))

for i in range(2, N+1):
    print(dist[i] if dist[i] != inf else -1)