import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def prim(start, case):
    pq = []
    
    heappush(pq, (0, start))

    distance = [1e9] * (V+1)
    distance[start] = 0
    while pq:
        dist, now = heappop(pq)
        dist *= -1
        if distance[now] < dist:
            continue

        for nxt_dist, to in link[now]:
            new_dist = dist + nxt_dist

            if distance[to] < new_dist:
                continue

            distance[to] = new_dist

            heappush(pq, (-new_dist, to))

    if case:
        return max(distance[1:])
    
    tmp = 0
    idx = 0
    for i in range(1, V+1):
        if distance[i] > tmp:
            tmp = distance[i]
            idx = i
    return idx


V = int(input())
link = [[] for _ in range(V+1)]
for _ in range(V):
    v, *edge, end = map(int, input().split())
    for i in range(len(edge)//2):
        link[v].append([edge[i*2+1], edge[i*2]])

node = prim(1, 0)
print(prim(node, 1))