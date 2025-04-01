import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())

start_prob = [True for _ in range(N+1)]
prev_prob = {i:[] for i in range(1, N+1)}
deg = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    prev_prob[A].append(B)
    
    start_prob[B] = False
    deg[B] += 1

que = []

for i in range(1, N+1):
    if start_prob[i]:
        heappush(que, i)

ans = []

while que:
    v = heappop(que)
    ans.append(v)

    for prev in prev_prob[v]:
        deg[prev] -= 1
        if not deg[prev]:
            heappush(que, prev)

print(*ans)
