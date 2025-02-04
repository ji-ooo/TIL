import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

N, H, T = map(int, input().split())
heights = [-int(input()) for _ in range(N)]

heapify(heights)

cnt = 0

while T > 0:
    now = -heights[0]
    if now == 1 or now < H:
        break
            
    heappush(heights, -(-heappop(heights)//2))

    cnt += 1
    T -= 1

last = -heights[0]
if last < H:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(last)