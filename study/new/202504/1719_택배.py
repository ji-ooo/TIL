import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')

dist = [[INF] * n for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    s, e, t = map(int, input().split())
    s -= 1
    e -= 1
    if t < dist[s][e]:
        dist[s][e] = dist[e][s] = t
        visited[s][e] = e
        visited[e][s] = s

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                visited[i][j] = visited[i][k]

for i in range(n):
    for j in range(n):
        if visited[i][j] == -1:
            visited[i][j] = '-'
        else:
            visited[i][j] += 1

for a in visited:
    print(*a)