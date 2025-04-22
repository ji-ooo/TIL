import sys
input = sys.stdin.readline

N = int(input())

balls = []

for i in range(N):
    c, v = map(int, input().split())
    balls.append((c, v, i))

balls.sort(key=lambda x: x[1])
ans = [0] * N

color = [0] * (N+1)
total = 0

idx = 0
for c, v, i in balls:
    
    while balls[idx][1] < v:
        total += balls[idx][1]
        color[balls[idx][0]] += balls[idx][1]
        idx += 1

    ans[i] = total - color[c]

for a in ans:
    print(a)