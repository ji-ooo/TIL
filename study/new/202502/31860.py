import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N, M, K = map(int, input().split())
I = []

for _ in range(N):
    heappush(I, -int(input()))

Y = 0
day = 0
ans = []

while I:
    day += 1
    t = -heappop(I)

    Y //= 2
    Y += t

    t -= M
    if t > K:
        heappush(I, -t)
    ans.append(Y)

print(day)

for i in ans:
    print(i)
