import sys
sys.stdin = open('5247.txt')
from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    visited[N] = 0
    que = deque([N])
    result = 0
    while que:
        v = que.popleft()
        cnt = visited[v] + 1

        for x in (v+1, v-1, v*2, v-10):
            if 0 < x <= 1000000:
                if x == M:
                    result = cnt
                    break
                if not visited[x]:
                    visited[x] = cnt
                    que.append(x)

        if result:
            break

    print(f'#{tc} {result}')

    # visited = {}
    # result = 0
    # while que:
    #     v = que.popleft()
    #     i, cnt = v
    #     cnt += 1
    #     for x in (i+1, i-1, i*2, i-10):
    #         if 0 <= x <= 1000000:
    #             if x == M:
    #                 result = cnt
    #                 break
    #             if x not in visited:
    #                 visited[x] = cnt
    #                 que.append((x, cnt))
    #
    #     if result:
    #         break
    #
    # print(f'#{tc} {result}')
