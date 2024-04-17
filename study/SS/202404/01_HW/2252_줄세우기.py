import sys
input = sys.stdin.readline

N, M = map(int, input().split())
link = {i:[] for i in range(N+1)}
rev_link = {i:[] for i in range(N+1)}
start = {i for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    if b in start:
        start.remove(b)
    link[a].append(b)
    rev_link[b].append(a)

line = []
while start:
    v = start.pop()
    line.append(v)
    for i in link[v]:
        rev_link[i].remove(v)
        if not rev_link[i]:
            start.add(i)
print(*line)
