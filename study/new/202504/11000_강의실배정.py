import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())

hp = []
for _ in range(n):
    s, e = map(int, input().split())
    heappush(hp, (s, 1))
    heappush(hp, (e, -1))

cnt = 0
ans = 0
while hp:
    cl, v = heappop(hp)
    cnt += v
    ans = max(cnt, ans)

print(ans)