import sys
sys.stdin = open('5249.txt')
from heapq import heappush, heappop


def prim(start):
    pq = []
    heappush(pq, (0, start))

    MST = [0] * (V+1)

    weight_sum = 0
    while pq:
        weight, now = heappop(pq)

        if MST[now]:
            continue

        MST[now] = 1

        weight_sum += weight

        for to in link[now]:
            next_w, nxt = to
            if MST[nxt]:
                continue
            else:
                heappush(pq, (next_w, nxt))

    print(f'#{tc} {weight_sum}')


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    link = [[] for _ in range(V+1)]

    distance = [0] * (V+1)
    for _ in range(E):
        n1, n2, w = map(int, input().split())

        link[n1].append([w, n2])
        link[n2].append([w, n1])

    prim(0)

