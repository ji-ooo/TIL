import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input())

que = []

for _ in range(N):
    n, s, e = map(int, input().split())

    heappush(que, (s, 1))
    heappush(que, (e, -1))

cnt = 0
ans = 0

while que:
    t, v = heappop(que)

    cnt += v

    ans = max(ans, cnt)

print(ans)
