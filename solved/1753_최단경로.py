import sys
input = sys.stdin.readline
from heapq import heappush, heappop

V, E = map(int, input().split())
link = [[] for _ in range(V+1)]

K = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    link[u].append([w, v])

distance = [1e9] * (V+1)
distance[0] = distance[K] = 0


pq = []
heappush(pq, (0, K))

while pq:
    dist, now = heappop(pq)

    if distance[now] < dist:
        continue

    for nxt_dist, to in link[now]:
        new_dist = dist + nxt_dist
        if distance[to] <= new_dist:
            continue

        distance[to] = new_dist
        heappush(pq, (new_dist, to))

for i in range(1, V+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])
