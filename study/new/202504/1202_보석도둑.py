import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def sol(jewel, bags):
    jewel.sort(reverse=True)
    bags.sort()

    pq = []
    ans = 0
    for bag in bags:

        while jewel:
            w, v = jewel.pop()

            if w <= bag:
                heappush(pq, -v)
            else:
                jewel.append((w, v))
                break
        
        if pq:
            ans -= heappop(pq)
    
    return ans


N, K = map(int, input().split())

jewel = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

print(sol(jewel, bags))