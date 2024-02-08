import sys
sys.stdin = open('5097.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    que = deque(list(map(int, input().split())))

    for _ in range(M):
        que.append(que.popleft())

    print(f'#{tc} {que.popleft()}')