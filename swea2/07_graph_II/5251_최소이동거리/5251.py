import sys
sys.stdin = open('5251.txt')

from heapq import heappush, heappop


def dijk(start):
    pq = []
    distance = [1e9] * (N+1)
    distance[0] = 0
    heappush(pq, (0, start))

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for nxt_dist, to in link[now]:
            nxt = nxt_dist + dist
            if distance[to] <= nxt:
                continue

            distance[to] = nxt
            heappush(pq, (nxt, to))
    print(f'#{tc} {distance[N]}')


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())

    link = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        link[s].append([w, e])

    dijk(0)