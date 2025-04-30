import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
link = {i:[] for i in range(1, N+1)}
deg = [0] * (N+1)
time = [0] * (N+1)
start = [True] * (N+1)

for i in range(N):
    id = i + 1

    line = list(map(int, input().split()))
    time[id] = line[0]

    tmp = line[1:-1]
    if tmp:
        deg[id] += len(tmp)
        start[id] = False
        
        for x in tmp:
            link[x].append(id)

hq = []
visited = [0] * (N+1)
for i in range(1, N+1):
    if start[i]:
        heappush(hq, (time[i], i))
        visited[i] = time[i]

while hq:
    t, v = heappop(hq)

    for nxt in link[v]:
        deg[nxt] -= 1
        
        if not deg[nxt]:
            if not visited[nxt]:
                heappush(hq, (t + time[nxt], nxt))
                visited[nxt] = t + time[nxt]

for i in range(1, N+1):
    print(visited[i])